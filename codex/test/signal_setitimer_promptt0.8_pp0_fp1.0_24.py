import signal
# Test signal.setitimer(): timer
# stopped after a blocking system call
# in the handler.

class alarm_handler(object):
    def __init__(self):
        self.triggered = False

