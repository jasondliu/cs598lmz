gi = (i for i in ())
# Test gi.gi_code.co_flags

def g(): yield 1
gi = g()
# Test gi.gi_frame.f_lasti

def g(): yield 1
gi = g()
gi.next()
# Test gi.gi_frame.f_locals

def g(): yield 1
gi = g()
gi.next()
# Test gi.gi_frame.f_trace

def g(): yield 1
gi = g()
gi.next()
# Test gi.gi_frame.f_exc_type

def g(): yield 1
gi = g()
gi.next()
# Test gi.gi_frame.f_exc_value

def g(): yield 1
gi = g()
gi.next()
# Test gi.gi_frame.f_exc_traceback

def g(): yield 1
gi = g()
gi.next()
# Test gi.gi_frame.f_restricted

def g(): yield 1
gi = g()
gi.next()
# Test gi.gi_frame.f_builtins

def g(): yield
