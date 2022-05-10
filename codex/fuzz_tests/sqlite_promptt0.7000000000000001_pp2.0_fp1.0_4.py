import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("test.db").execute("create table t1(i1, i2);")

from .. import _gpgme, util

def _check_null(res, func, args):
    if res is None:
        raise ValueError('function returned NULL')
    return res

# If a function is declared as returning a char*, we want to convert it
# to a Python string.  Since ctypes doesn't know about constness, we have
# to special-case the const-qualified char* return types.
def _return_char_p(res, func, args):
    return util._to_unicode_maybe(res)

_gpgme_new_signature_p = _gpgme.gpgme_new_signature_p
_gpgme_new_signature_p.restype = ctypes.POINTER(_gpgme.gpgme_signature_t)
_gpgme_new_signature_p.errcheck = _check_null

_gpgme_op_verify_result_p = _gpgme.gpgme
