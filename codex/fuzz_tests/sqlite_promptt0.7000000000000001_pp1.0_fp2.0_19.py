import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
try:
    sqlite3.connect('test.db')
except:
    print 'sqlite3 missing or not install correctly'
    exit(-1)

# Test zlib.decompressobj
try:
    from zlib import decompressobj
except:
    print 'zlib missing or not install correctly'
    exit(-1)

# Test ctypes
try:
    ctypes.util.find_library('ssl')
    ctypes.util.find_library('crypto')
except:
    print 'ssl missing or not install correctly'
    exit(-1)

# Test python-ldap
try:
    import ldap
except:
    print 'python-ldap missing or not install correctly'
    exit(-1)

# Test cjson
try:
    import cjson
except:
    print 'python-cjson missing or not install correctly'
    exit(-1)

# Test M2Crypto
try:
    import M2Crypto
except:
    print 'python-m2crypto missing or not install correctly'
    exit(-
