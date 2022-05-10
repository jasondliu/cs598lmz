import select
import datetime
import time
import sys

#global variable
global_time = 0
global_data = {}
global_data_str = {}
global_data_str_temp = {}
global_data_str_hum = {}
global_data_str_press = {}
global_data_str_wind = {}



#define the function to send the data
def send_data(data):
    global global_data
    global global_time
    global global_data_str
    global global_data_str_temp
    global global_data_str_hum
    global global_data_str_press
    global global_data_str_wind

    global_data[data] = global_time
    global_time += 1

    if data == 'temp':
        global_data_str_temp[global_time] = global_data[data]
    elif data == 'hum':
        global_data_str_hum[global_time] = global_data[data]
    elif data == 'press':
        global_data_str_press[global_time]
