import signal
# Test signal.setitimer()

#
# Test 1:
#
# test signal.setitimer()
#
print('Test setitimer: ', end='')

def handler(signum, frame):
    raise Exception("signal handler called")

# save old signal handler
old = signal.signal(signal.SIGALRM, handler)

# try a timer
signal.setitimer(signal.ITIMER_REAL, 0.2)
time.sleep(1)

# restore the old signal handler
signal.signal(signal.SIGALRM, old)

print("OK")
