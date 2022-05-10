gi = (i for i in ())
# Test gi.gi_code
# Test gi.gi_name
# Test gi.gi_frame
# Test gi.gi_running
# Test gi.gi_frame.f_lasti
# Test gi.gi_frame.f_lineno
# Test gi.gi_frame.f_trace
# Test gi.gi_frame.f_exc_type
# Test gi.gi_frame.f_exc_value
# Test gi.gi_frame.f_exc_traceback


# Test the effect of sys.settrace() on sys.exc_traceback

import sys
leak_tracker_1 = []
leak_tracker_2 = []

class Tracer(object):
    def __init__(self, tracker):
        self.tracker = tracker
    def __call__(self, frame, event, arg):
        self.tracker.append(event)
        if event == 'exception':
            self.tracker.append(arg)
            self.tracker.append(sys.exc_traceback)
        return self

def exception_
