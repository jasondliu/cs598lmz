import signal
# Test signal.setitimer
def handler(num, v):
    pass

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 0)
print("Begin of the program")
i = 0
while True:
    i += 1
    if i % 100000 == 0:
        print(".", end='', flush=True)
print("End of the program")
