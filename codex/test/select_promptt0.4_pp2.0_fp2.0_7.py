import select
# Test select.select()

import sys
import time

if sys.platform.startswith('win'):
    timefunc = time.clock
else:
    timefunc = time.time

def f():
    for i in range(5):
        print(i)
        time.sleep(1)

def f2():
    for i in range(5):
        print(i)
        time.sleep(1)

start = timefunc()

thread.start_new_thread(f, ())
thread.start_new_thread(f2, ())

time.sleep(6)

end = timefunc()

