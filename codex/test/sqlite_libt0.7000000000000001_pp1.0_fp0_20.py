import ctypes
import ctypes.util
import threading
import sqlite3
import ssl
import base64

PORT = 4433

def or_die(val, msg):
    if val < 0:
        print('Error:', msg)
        exit(1)
    return val

def serve(ctx, cb):
    l = or_die(lib.gnutls_priority_init('NORMAL', None),
               'Error in initialization')
    psk_key = ctypes.create_string_buffer(base64.b64encode(b'\x01\x02\x03\x04'))
    psk_key_len = ctypes.c_uint(4)
    psk_cred = ctypes.pointer(lib.gnutls_psk_server_credentials_t())
    or_die(lib.gnutls_psk_allocate_server_credentials(ctypes.byref(psk_cred)),
           'Error in credentials allocation')
