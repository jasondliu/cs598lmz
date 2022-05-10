import signal
# Test signal.setitimer

def handler(sig, frame):
    print('handler')
    signal.alarm(0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)
start = time.time()
while True:
    print('loop', time.time() - start)
    time.sleep(1)
