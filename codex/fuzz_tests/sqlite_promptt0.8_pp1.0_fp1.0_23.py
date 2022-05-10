import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# conn = sqlite3.connect('log/mydatabase.db')
# print "Opened database successfully";
# conn.close()

# create thread for epe_callback()
epe_thread = threading.Thread(target=epe_callback)

# start epe_thread
epe_thread.start()

# initialize EPE
epe_initialize()

# open serial port
if epe_open('COM1') != 0:
    print 'Cannot open port';
    exit(1)

# set serial port
if epe_set_serial(EPE_BAUDRATE_9600, EPE_DATABITS_8, EPE_PARITY_NONE, EPE_STOPBITS_1, EPE_FLOWCTRL_NONE) != 0:
    print 'Cannot set serial port';
    exit(1)

# set sensor configuration
if epe_set_sensorconfig(EPE_SENSORCONFIG_INIT | EPE_SENSORCONFIG_METRIC) != 0:

