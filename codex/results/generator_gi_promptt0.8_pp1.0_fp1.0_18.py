gi = (i for i in ())
# Test gi.gi_code
gi.gi_code.co_name
gi.gi_code.co_freevars
gi.gi_code.co_argcount
# Test gi.gi_frame
gi.gi_frame.f_code.co_name
gi.gi_frame.f_code.co_freevars
gi.gi_frame.f_code.co_argcount
gi.gi_frame.f_locals
gi.gi_frame.f_locals["gi"]
gi.gi_frame.f_lineno
gi.gi_frame.f_globals
gi.gi_frame.f_back is None
gi.gi_frame.f_trace is None
gi.gi_frame.f_exc_type is None
gi.gi_frame.f_exc_value is None
gi.gi_frame.f_exc_traceback is None
# Import dis
import dis
dis.dis(gi.gi_code)
# Test gi.gi_yieldfrom
gi.gi_yieldfrom is None
# Test gi.gi_running
gi.gi_
