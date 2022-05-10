import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

libcrypto_path = ctypes.util.find_library('crypto')
if not libcrypto_path:
    raise ImportError('Cannot find crypto library')
libcrypto = ctypes.CDLL(libcrypto_path)

# typedef struct _EVP_CIPHER_CTX_st EVP_CIPHER_CTX;
class _EVP_CIPHER_CTX_st(ctypes.Structure):
    pass
EVP_CIPHER_CTX = _EVP_CIPHER_CTX_st

# int EVP_CIPHER_CTX_reset(EVP_CIPHER_CTX *c)
libcrypto.EVP_CIPHER_CTX_reset.restype = ctypes.c_int
libcrypto.EVP_CIPHER_CTX_reset.argtypes = [ctypes.POINTER(EVP_CIPHER_CTX)]

# int EVP_CIPHER_CTX_init(EVP_CIPHER_CTX *
