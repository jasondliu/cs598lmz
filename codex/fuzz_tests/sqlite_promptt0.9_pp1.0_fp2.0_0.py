import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')
import base64
import random
import zmq

from Crypto.Cipher import AES
from Crypto import Random

import os


############## Socket for the COM port ##############
# Initialize bluetooth socket
master_bluetooth_port='00:06:66:66:17:E1'
socket=BluetoothSocket(RFCOMM)
socket.connect((master_bluetooth_port,1))
print("DONE CONNECTED")

# Print error if bluetooth port not available
if (!socket):
    print("ERROR CONNECTING BLUETOOTH")
#####################################################

############## VARIABLES FOR DECRYPTION ##############
cipher = ""
cipher_obj = ""
iv = ""
key = ""
#####################################################

############## Class ##############
### Inserts hrm values into arrays
class GetMetric(threading.Thread):
    def __init__(self,hr=[]):
        threading.Thread.__init__(self)
        self.hr = hr
