import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("Alarm!")

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1)

try:
    while True:
        print("Waiting...")
        time.sleep(1)
except KeyboardInterrupt:
    print("done.")

signal.setitimer(signal.ITIMER_REAL, 0)

#
#     $ python3 signal_setitimer.py
#     Waiting...
#     Alarm!
#     Waiting...
#     Alarm!
#     Waiting...
#     Alarm!
#     Waiting...
#     Alarm!
#     Waiting...
#     Alarm!
#     Waiting...
#     Alarm!
#     Waiting...
#     Alarm!
#     Waiting...
#     Alarm!
#     Waiting...
#     Alarm!
#     Waiting...
#     Alarm!
#     Waiting...
#     Alarm!
#     Waiting
