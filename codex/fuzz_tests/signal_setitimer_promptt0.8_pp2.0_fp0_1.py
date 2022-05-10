import signal
# Test signal.setitimer(signal.ITIMER_VIRTUAL, 1, 1)
# It works on Linux and Mac, but not on Windows
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 1)

# On Windows, clock() returns wall-clock time, not CPU time as in Unix
# On Windows, time.clock measures wall-clock time,
# time.perf_counter() and time.process_time() measure CPU time

import time

def show_clock(name, clock):
    elapsed = 0
    for i in range(5):
        t0 = clock()
        while clock() - t0 < 1:
            pass
        print(name, clock() - t0)
        elapsed += clock() - t0
    print('total', elapsed)

show_clock('clock      :', time.clock)
show_clock('perf_counter:', time.perf_counter)

try:
    show_clock('process_time:', time.process_time)
except AttributeError:
    print('Windows: no process_time')
