import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

for sig in [signal.SIGALRM, signal.SIGVTALRM, signal.SIGPROF]:
    signal.signal(sig, handler)

def mainloop():
    while delays:
        time.sleep(0.1)

print('Starting', time.time())
signal.setitimer(signal.ITIMER_REAL, delays.pop())
mainloop()
print('Ending', time.time())

# Example:
#
# Starting 1497959349.0967426
# SIGALRM 1497959349.0968506
# SIGVTALRM 1497959349.0970492
# SIGPROF 1497959349.0971509
# SIGALRM 1497959349.0973476
# SIGVTALRM 1497959349.0975546
# SIGPROF 1497959349.0977515
# ...
# SIGPROF 1497959349.1700785
# SIGALRM 1497959349.170179
# SIGVTALRM 1497959349.1702819
# SIGPROF
