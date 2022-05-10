import signal
# Test signal.setitimer() and signal.getitimer()
def get_itimer_test(sig, frame):
    print('get itimer test')

signal.signal(signal.SIGPROF, get_itimer_test)

# signal.setitimer(which, seconds, interval)
# which: ITIMER_PROF, ITIMER_REAL, ITIMER_VIRTUAL
print('set itimer')
signal.setitimer(signal.ITIMER_PROF, 2, 1)
time.sleep(10)
print('get itimer')
print(signal.getitimer(signal.ITIMER_PROF))

# Test signal.set_wakeup_fd()
def signal_wakeup_test(sig, frame):
    print('signal wakeup test')

# fd: file object, must be open
signal.signal(signal.SIGALRM, signal_wakeup_test)
signal.set_wakeup_fd(sys.stdout.fileno())
time.sleep(10)
sign
