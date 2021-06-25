#!/usr/bin/env python
# coding: utf-8


import socket
import numpy as np
import tkinter as tk
from tkinter.ttk import *
from pytz import timezone
from PIL import ImageTk, Image
from tkcalendar import Calendar

"""

This module uses tkinter library to get user input from GUI window

"""

def get_values():

    """ get_values gives the values in the form of dict :
     params_dict= {'obsDate':str (yyyy-mm-dd),
    'AltPlot': bool,
    'AirMassPlot': bool, 
    'SaveBothPlots': bool,
    'ObjSkyPlot':bool,
    'Object': str , 
    'RA': str (hh:mm:ss),
    'Dec': str (dd:mm:ss)}
    """
    
    def grad_date():
        date.config(text = "Selected Date is: " + cal.get_date())

    def close_window():
        top.destroy()

    top = tk.Tk()
    top.title('Object Visibility Plots at HCT, IAO')
    top.resizable(True, True)
    top.configure(bg='black')


    CheckVarAlt = tk.IntVar(top)
    CheckVarAirmass = tk.IntVar(top)
    SavePlots = tk.IntVar(top)
    ObjSky = tk.IntVar(top)
    NameObject = tk.StringVar(top)
    RA_Object = tk.StringVar(top)
    Dec_Object = tk.StringVar(top)

    plot_for_altitude = tk.Checkbutton(top, text='Alt. v Time Plot', selectcolor='blue',
                                       variable= CheckVarAlt,fg='white',bg='black',activebackground='red',
                                       onvalue=1, offvalue=0, height=6, width=20, anchor='w', font=('Havletica', 12))
    plot_for_airmass = tk.Checkbutton(top, text='Airmass v Time Plot',selectcolor='blue',
                                      variable=CheckVarAirmass,fg='white',bg='black',activebackground='red',
                                      onvalue=1, offvalue=0, height=6, width=20, anchor='w', font=('Havletica', 12))

    save_plots = tk.Checkbutton(top, text='Save Plots', variable=SavePlots,activebackground='red',
                                onvalue=1,fg='white',bg='black',selectcolor='blue',
                               offvalue=0, height=6, width=20, anchor='w', font=('Havletica', 12))

    obj_finder_plot = tk.Checkbutton(top, text='Object in Sky Plot', variable=ObjSky,activebackground='red',
                                onvalue=1,fg='white',bg='black',selectcolor='blue',
                               offvalue=0, height=6, width=20, anchor='w', font=('Havletica', 12))

    cal = Calendar(top, selectmode='day', date_pattern='yyyy mm dd')
    date = tk.Label(top, text='Select Obs Day ', fg='white', bg='black',font=('DejaVu',12))
    close_button = tk.Button(top, text = "Click and Quit", command = close_window,font=('DejaVu',12), bg='white',fg='red')


    Object_params = tk.Label(top, text='Write Object Properties', font=("DejaVu", 14),
                             fg='yellow', bg='black', padx=4,pady=4)
    Plot_params = tk.Label(top, text=' Plot Options (Choose Multiple)', font=("DejaVu", 14),
                           fg='red', bg='black', padx=4,pady=4)

    Object_name = tk.Label(top, text=' Name of the Object', bg='black',fg='white',font=('Havletica', 12))
    Object_name_entry = tk.Entry(top, bd=5, textvariable=NameObject,font=('Havletica', 12))

    Object_RA = tk.Label(top, text=" Object's RA (hh:mm:ss)",bg='black', fg='white', font=('Havletica', 12))
    Object_RA_entry = tk.Entry(top, bd=5, textvariable=RA_Object,font=('Havletica', 12))

    Object_dec = tk.Label(top, text = "Object's dec (dd:mm:ss)", bg='black', fg='white', font=('Havletica', 12))
    Object_dec_entry = tk.Entry(top, bd=5, textvariable=Dec_Object,font=('Havletica', 12))

    Object_params.grid(row=0, columnspan=2, column=0)
    Plot_params.grid(row=0, columnspan=2, column=2)


    Object_name.grid(row=1,column=0)
    Object_name_entry.grid(row=1,column=1)
    Object_RA.grid(row=2,column=0)
    Object_RA_entry.grid(row=2,column=1)
    Object_dec.grid(row=3,column=0)
    Object_dec_entry.grid(row=3,column=1)

    date.grid(row=4, columnspan=2)
    cal.grid(row=5, columnspan=2, rowspan=2, column=0)
    plot_for_altitude.grid(row=1, column=3)
    plot_for_airmass.grid(row=2, column=3)
    obj_finder_plot.grid(row=3, column=3)
    save_plots.grid(row=4, column=3)
    close_button.grid(row=6, column=2)

    for i in range(11):
        top.grid_rowconfigure(i, weight=1)
    top.grid_columnconfigure(0,weight=1)
    top.grid_columnconfigure(1,weight=1)


    top.mainloop()
    
    params_dict= {'obsDate':cal.get_date(),
    'AltPlot': CheckVarAlt.get(),
    'AirMassPlot': CheckVarAirmass.get(), 
    'SaveBothPlots': SavePlots.get(),
    'ObjSkyPlot':ObjSky.get(),
    'Object': NameObject.get(), 
    'RA': RA_Object.get(),
    'Dec': Dec_Object.get() }
    
    return params_dict

if __name__ == "__main__":
	get_values()

