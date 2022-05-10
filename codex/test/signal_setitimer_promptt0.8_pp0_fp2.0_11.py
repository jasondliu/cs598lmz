import signal
# Test signal.setitimer()
start_time = time.time()

def handle_alarm(signum, frame):
    if time.time() - start_time > 2:
        print('Sleeping for 10s...')
        signal.setitimer(signal.ITIMER_REAL, 10)
        return
    print('Exiting...')
    sys.exit(0)

signal.signal(signal.SIGALRM, handle_alarm)
signal.setitimer(signal.ITIMER_REAL, 1)

while True:
    pass
