import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.2)

# Test signal.getitimer
print(signal.getitimer(signal.ITIMER_REAL))

# Test signal.signal
def handler(signum, frame):
    print('Received signal', signum)

signal.signal(signal.SIGALRM, handler)
signal.alarm(1)

print('Sleeping for 2 seconds')
time.sleep(2)

# Test signal.getsignal
print(signal.getsignal(signal.SIGALRM))

# Test signal.pause
print('Sleeping for 2 seconds')
time.sleep(2)
print('Pausing')
signal.pause()

# Test signal.pthread_kill
signal.pthread_kill(threading.get_ident(), signal.SIGUSR1)

# Test signal.pthread_
