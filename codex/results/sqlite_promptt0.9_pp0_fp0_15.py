import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# db = sqlite3.connect(":memory:")
# Test sqlite3.connect

# Including this definition
def defaultCallback(user_data):
    print(user_data)

contact_cb_t = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

# Set up prototype and parameters for the ctype callback
callback_type = contact_cb_t(defaultCallback)

# # Alternative callback would be
# def altCallback(user_data):
#     newString = "Hello, World: " + user_data
#     print(newString)

# callback_type = contact_cb_t(altCallback)


# Initialize the library

nfc_init = ctypes.cdll.LoadLibrary('./libnfc.so')


# Initialize the NFC device
nfc_device = nfc.nfc_device()
pnd = ctypes.pointer(nfc_device)

# possible values are:
# {NONE, LOG_NONE, LOG_CRITICAL, LOG_ERROR, LOG_
