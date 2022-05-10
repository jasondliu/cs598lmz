import signal
# Test signal.setitimer with signal.ITIMER_VIRTUAL
import signal, time

def alarm_handler(signum, frame):
    print('Got signal', signum)
    global alarm_fired
    alarm_fired = True

alarm_fired = False
old_handler = signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_VIRTUAL, 1)
print('Sleeping')
time.sleep(5)
if not alarm_fired:
    print('5 seconds passed with no alarm')
print('Disarming timer')
signal.setitimer(signal.ITIMER_VIRTUAL, 0)
