import threading
# Test threading daemon
import time


def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    print('wait_for_event: starting')
    event_is_set = e.wait()
    print('event set: %s', event_is_set)


def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    while not e.isSet():
        print('wait_for_event_timeout: starting')
        event_is_set = e.wait(t)
        print('event set: %s', event_is_set)
        if event_is_set:
            print('processing event')
        else:
            print('doing other work')


# Test threading
def threading_function(name):
    print('threading_function: starting')
    time.sleep(2)
    print('threading_function: ending')


# Test threading lock
class Counter(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
