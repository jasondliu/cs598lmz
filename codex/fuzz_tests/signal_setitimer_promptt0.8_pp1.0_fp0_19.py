import signal
# Test signal.setitimer

def handler_alarm(sig, frame):
    print("Got alarm.")


def handler_prof(sig, frame):
    print("Got prof.")


signal.signal(signal.SIGALRM, handler_alarm)
signal.signal(signal.SIGPROF, handler_prof)

print("Before setitimer")
signal.setitimer(signal.ITIMER_REAL, .2, .2)
print("After setitimer")
for i in range(10):
    print("sleeping", i)
    time.sleep(1)
