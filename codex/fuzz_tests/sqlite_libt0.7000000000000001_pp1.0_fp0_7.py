import ctypes
import ctypes.util
import threading
import sqlite3
import json

# Load the C library
lib = ctypes.CDLL(ctypes.util.find_library("Pkcs11Wrapper"))

# Load the C types
C_CK_SLOT_ID = ctypes.c_ulong
C_CK_OBJECT_HANDLE = ctypes.c_ulong
C_CK_SESSION_HANDLE = ctypes.c_ulong
C_CK_FUNCTION_LIST_PTR = ctypes.POINTER(ctypes.c_long)
C_CK_UTF8CHAR_PTR = ctypes.c_char_p
C_CK_BYTE_PTR = ctypes.c_char_p
C_CK_ULONG = ctypes.c_ulong

# Define the CKK_* types
CKK_RSA = 0x00000000
CKK_DSA = 0x00000001
CKK_DH = 0x00000002

# Define the CK_ATTRIBUTE_TYPE values
CKA_TOKEN = 0x00000001
C
