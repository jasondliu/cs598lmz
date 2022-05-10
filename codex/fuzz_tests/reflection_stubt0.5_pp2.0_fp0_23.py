fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
sys.settrace(fn)

# This will cause a crash:
#   File "test_crash.py", line 19, in <module>
#     sys.settrace(fn)
#   File "/usr/lib/python3.7/bdb.py", line 88, in trace_dispatch
#     return self.dispatch_line(frame)
#   File "/usr/lib/python3.7/bdb.py", line 112, in dispatch_line
#     if self.quitting: raise BdbQuit
# bdb.BdbQuit
