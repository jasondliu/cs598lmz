import select
# Test select.select timeout. Issue #10510.
import os, threading, time
r, w, _ = select.select([], [], [], 1)

class E(Exception):
    pass

def read():
    while True:
        time.sleep(1)
        try:
            r, _, _ = select.select([os.open('', os.O_RDONLY)], [], [], 30)
        except E:
            return
        else:
            raise E

class T(threading.Thread):
    def __init__(self, *args, **kw):
        super(T, self).__init__(*args, **kw)
        self.start()

class S(T):
    def run(self):
        time.sleep(1)
        raise E

S()
read()

class S(T):
    def run(self):
        time.sleep(0.3)
        raise E
    def cancel(self):
        pass

S()
read()
###############################################################################

# select.select follow-up from
