gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_running
gi.gi_running
# Test gi.gi_frame.f_lasti
gi.gi_frame.f_lasti
# Test gi.gi_frame.f_trace
gi.gi_frame.f_trace
# Test gi.gi_frame.f_exc_type
gi.gi_frame.f_exc_type
# Test gi.gi_frame.f_exc_value
gi.gi_frame.f_exc_value
# Test gi.gi_frame.f_exc_traceback
gi.gi_frame.f_exc_traceback

# Test when array is resized gi_frame.f_local is updated
# Bug #1587906
import sys

def func():
    global x
    x = 1
    sys._getframe()

x = [None]*1000000
func()
x[-1]

# Test gi.gi_frame.f_back
def func():

