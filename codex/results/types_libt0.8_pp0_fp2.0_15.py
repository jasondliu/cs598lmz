import types
types.CodeType

import sys
sys.setrecursionlimit(8000)
'''
#for python2
import types
import sys

def trace_calls(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    func_line_no = frame.f_lineno
    func_filename = co.co_filename
    caller = frame.f_back
    caller_line_no = caller.f_lineno
    caller_filename = caller.f_code.co_filename
    print ('Call to %s on line %s of %s from line %s of %s' % \
        (func_name, func_line_no, func_filename,
            caller_line_no, caller_filename))
    return

def install_trace():
    sys.settrace(trace_calls)

def remove_trace():
    sys.settrace(None)


