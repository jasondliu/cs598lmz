import weakref
# Test weakref.ref(obj)
# Test weakref.ref(obj, callback)
# Test weakref.proxy(obj)
# Test weakref.proxy(obj, callback)

import weakref

def callback(obj):
    print "Dead:", obj

def test_ref_callback():
    s = "hello"
    ref = weakref.ref(s, callback)
    print ref
    del s
    print ref
    print "-" * 20
    print ref()

def test_ref_no_callback():
    s = "hello"
    ref = weakref.ref(s)
    print ref
    del s
    print ref
    print "-" * 20
    print ref()

def test_proxy():
    s = "hello"
    proxy = weakref.proxy(s)
    print proxy
    print proxy + " world"
    print "-" * 20
    del s
    try:
        print proxy
    except ReferenceError:
        print "ReferenceError"

def test_proxy_callback():
    s = "hello"
    proxy = weakref.
