import ctypes
import ctypes.util
import threading
import sqlite3
import os

BaseName = 'libvmod-querystring'

# list of available functions, with argument types
_lib = {
    'VRT_InitVmod': [ctypes.c_void_p, ],
    'VRT_SetHooks': [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p],
    'VRT_priv_fini': [],
    'VRT_priv_task': [],
    'VRT_priv_storage': [],
    'VRT_public_fini': [],
    'VRT_public_task': [],
    'VRT_public_storage': [],
    'VRT_std_core_vcl': [],
    'VRT_synth_page': [],
    'VRT_VCL_conf': [],
    'VRT_VCL_dir': [],
    'VRT_VCL_dir_conf': [],
    'VRT_VCL_init': [
