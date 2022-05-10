import weakref
# Test weakref.ref(int), which was broken by r80765
weakref.ref(int)

import datetime
assert datetime.tzinfo.__module__ == 'datetime'

# Test reopening of socket.socket and socket.socket.__new__.
import socket
assert isinstance(socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.socket)

def test_openssl():
    import _ssl
    try:
        _ssl.SSLContext(0x0301)
    except ValueError as exc:
        if '0x301' in str(exc):
            raise Exception("Failed to build SSLContext with TLSv1.1")
        raise

test_openssl()

# Test the C implementation of weakref.ref() and weakref.proxy()
try:
    import _weakref
    import weakref
    r = _weakref.ref(range(10))
    p = _weakref.proxy(range(10))
    assert r() is p
    assert type(p) is weakref.ReferenceType
    try:
       
