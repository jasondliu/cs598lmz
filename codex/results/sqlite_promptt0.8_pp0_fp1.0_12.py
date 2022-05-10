import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('pythonsqlite.db')
import os
import time

# Cargamos las funciones auxiliares
import AuxiliarFunctions as aux

# Busco la ruta del archivo .so que contiene las funciones desde el cual voy a llamar
_file = '../lib/libSockets.so'
_path = os.path.join(*(os.path.split(_file)[:-1]))
_file = os.path.basename(_file)
# Cargamos la librería dinámica desde Sockets
aux.dprint("Cargando librería desde: "+_path+"/"+_file)
aux.dprint("=====================================")
lib = ctypes.cdll.LoadLibrary(_path+"/"+_file)

# Definimos los tipos de los parametros de las funciones que vamos a llamar
lib.crearSocket.argtypes = [ctypes.c_uint8]
lib.crearSocket.restype = ctypes.c_int
lib.en
