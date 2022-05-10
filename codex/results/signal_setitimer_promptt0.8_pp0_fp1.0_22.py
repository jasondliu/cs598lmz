import signal
# Test signal.setitimer
class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm

def set_and_wait():
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, 0.1)
    try:
        signal.pause()
    except Alarm:
        return
    assert False

signal.set_wakeup_fd(sys.stdout.fileno())
set_and_wait()
print('ok')
