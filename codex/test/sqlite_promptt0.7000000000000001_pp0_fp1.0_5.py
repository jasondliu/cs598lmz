import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() in thread

# Python 2.7.6 on Ubuntu 14.04.4 LTS, x86_64
# $ python -V
# Python 2.7.6
# $ uname -a
# Linux ubuntu 3.13.0-76-generic #120-Ubuntu SMP Tue Jan 19 12:13:34 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux

libsqlite3 = ctypes.util.find_library('sqlite3')
if not libsqlite3:
    raise Exception('Can not find "sqlite3" library')

_CALLBACK_FUNC = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int32, ctypes.c_char_p)

def _callback(user_data, num_cols, values, names):
    print('Callback')
    print('  user_data:', user_data)
    print('  num_cols:', num_cols)
    print('  values:', values)
