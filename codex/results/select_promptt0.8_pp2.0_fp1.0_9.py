import select
# Test select.select()
# Create non-blocking socket
import socket
sock = socket.socket()
sock.setblocking(False)

def my_callback(arg1, arg2):
    print("my_callback was called with", arg1, arg2)

try:
    from select import kqueue, kevent
    kq = kqueue()
    def set_timer(interval, callback, *args):
        e = [kevent(ident=1, filter=select.KQ_FILTER_TIMER, flags=select.KQ_EV_ADD,
                    fflags=0, data=0, udata=None)]
        kq.control(e, 0, interval)
        while True:
            # Wait for events
            events = kq.control(None, 1, None)
            for e in events:
                if e.ident == 1:
                    callback(*args)
except ImportError:
    import threading
    def set_timer(interval, callback, *args):
        def loop():
            while True:
                time.sleep(interval)
               
