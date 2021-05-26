#!/usr/bin/env python
# coding: utf-8

import socket
import datetime
import numpy as np
import dict_from_gui
import astropy.units as u
from pytz import timezone
import matplotlib.pyplot as plt
from astropy.time import Time, TimeDelta
from astroplan import FixedTarget, Observer
from astropy.coordinates import SkyCoord, EarthLocation
from astroplan.plots import plot_altitude, dark_style_sheet, plot_finder_image, plot_airmass


timezoneIAO = timezone('Asia/Kolkata')
timezoneIAO = timezoneIAO.localize(datetime.datetime(2012, 7, 10, 12, 0))
hct = Observer.at_site('iao',timezone= timezoneIAO.tzinfo)

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

"""
params_dict= {'obsDate':cal.get_date(),
'AltPlot': CheckVarAlt.get(),
'AirMassPlot': CheckVarAirmass.get(), 
'SaveBothPlots': SavePlots.get(),
'ObjSkyPlot':ObjSky.get(),
'Object': NameObject.get(), 
'RA': RA_Object.get(),
'Dec': Dec_Object.get() }
"""
params_dict = dict_from_gui.get_values()



yyyy, mm, dd = params_dict['obsDate'].split(' ')
dd_next = str(int(dd)+1) 


obj_name = str(params_dict['Object'])
RA_hr, RA_minutes, RA_secs = params_dict['RA'].split(':')
dec_deg, dec_min, dec_secs = params_dict['Dec'].split(':')
ALTPLOT = int(params_dict['AltPlot'])
AIRMASSPLOT = int(params_dict['AirMassPlot'])
SAVEPLOTS = int(params_dict['SaveBothPlots'])
OBJSKYPLOT = int(params_dict['ObjSkyPlot'])



#Define Object 
RA = RA_hr+'h'+RA_minutes+'m'+RA_secs+'s'
DEC = dec_deg+'d'+dec_min+'m'+dec_secs+'s'

obj_coord = SkyCoord(ra=RA, dec=DEC)
obj = FixedTarget(coord=obj_coord, name=obj_name)

delta_t = TimeDelta(12.0*3600*u.s, scale='tai')




#define time intervals 
start_time = Time(yyyy+'-'+mm+'-'+dd+' 13:00:00')
delta_t = TimeDelta(12.0*3600*u.s, scale='tai')
observing_time = start_time + delta_t*np.linspace(0,1,100)



fig, ax = plt.subplots(figsize=(8,6))

ax.set_title('Time Variation')
if ALTPLOT and AIRMASSPLOT:
    plot_altitude(obj, hct, observing_time, brightness_shading=True,ax=ax,
                  airmass_yaxis=True)    
    ax.axhline(25,c='red')
    ax.legend([obj_name],shadow=True,loc='upper right')
    plt.show()
    if SAVEPLOTS:
        fig.savefig(obj_name.strip(' ')+'_AirmassAlt_plot_'+params_dict['obsDate'].replace(' ','-')+'.pdf',
                bbox_inches='tight')
elif AIRMASSPLOT:
    plot_airmass(obj, hct, observing_time,brightness_shading=True, ax=ax)    
    ax.legend([obj_name],shadow=True,loc='upper right')
    plt.show()
    if SAVEPLOTS:
        fig.savefig(obj_name.strip(' ')+'_airmass_plot_'+params_dict['obsDate'].replace(' ','-')+'.pdf',
                bbox_inches='tight')
    
elif ALTPLOT:
    plot_altitude(obj, hct, observing_time,brightness_shading=True,ax=ax)    
    ax.axhline(25,c='red')
    ax.legend([obj_name],shadow=True,loc='upper right')
    plt.show()
    if SAVEPLOTS:
        fig.savefig(obj_name.strip(' ')+'_alt_plot_'+params_dict['obsDate'].replace(' ','-')+'.pdf',
            bbox_inches='tight')
    

if OBJSKYPLOT:
    print("Checking Internet Connection To retrieve sky maps\n")
    if is_connected():
        import warnings
        warnings.filterwarnings('ignore')
        import matplotlib.pyplot as plt1
        fig1, ax1 = plt1.subplots(figsize=(6,6))
        plt1.axis('off')
        fig1.suptitle('ra='+RA+' dec='+DEC)
        ax1, hdu = plot_finder_image(obj,reticle=True,grid=True, fov_radius=10*u.arcmin)
        fig1.show()
        plt1.show()
        
        if SAVEPLOTS:
            fig1.savefig(obj_name.strip(' ')+'_sky_'+params_dict['obsDate'].replace(' ','-')+'.pdf',
                    bbox_inches='tight')
    else :
        print("No Internet Connection\nExiting. Have a nice night.")
        exit()
    
exit()

