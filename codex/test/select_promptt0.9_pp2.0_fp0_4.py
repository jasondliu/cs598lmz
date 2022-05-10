import select
# Test select.select this time, not just time.sleep. This means, assuming
# enough fds are open, we should be able to poll an fd on a different
# thread and raise an exception.

import traceback
started = None
evt = threading.Event()
def child():
    global started
    started = True
    try:
        r, w, x = select.select([], [], [], 0.5)
    except KeyboardInterrupt:
        evt.set()

thread.start_new_thread(child, ())
while not started:
    tim
