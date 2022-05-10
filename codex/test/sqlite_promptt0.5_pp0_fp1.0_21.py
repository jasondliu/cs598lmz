import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')

# Callback function for enumerating the devices
def enum_callback(handle, name, address, flags, user_data):
    print('Found device %s at %s' % (name, address))

# Callback function for enumerating the services
def enum_services_callback(handle, conn_handle, uuid, user_data):
    print('Found service %s' % (uuid))

# Callback function for enumerating the characteristics
def enum_characteristics_callback(handle, conn_handle, uuid, properties, user_data):
    print('Found characteristic %s' % (uuid))

# Callback function for enumerating the descriptors
def enum_descriptors_callback(handle, conn_handle, uuid, user_data):
    print('Found descriptor %s' % (uuid))

# Callback function for the read callback
