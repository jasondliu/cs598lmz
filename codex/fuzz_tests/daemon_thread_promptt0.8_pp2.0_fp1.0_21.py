import threading
# Test threading daemon
import time

def set_interval(func, sec):
    """
    DEMO
    """
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

# def print_time():
#     """
#     DEMO
#     """

#     print "From print_time", time.time()

# def print_some_times():
#     """
#     DEMO
#     """

#     print time.time()
#     set_interval(print_time, 1)
#     time.sleep(3)
#     print time.time()

# print_some_times()

def wait_and_kill(t):
    """
    DEMO
    """

    time.sleep(1)
    t.cancel()

# def print_time():
#     """
#     DEMO
#     """

#     print "From print_time", time.time()
#     print
