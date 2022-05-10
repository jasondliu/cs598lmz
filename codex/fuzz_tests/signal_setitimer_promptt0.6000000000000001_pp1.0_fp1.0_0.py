import signal
# Test signal.setitimer()

def handler(signum, frame):
    print("signum = {}, frame = {}".format(signum, frame))

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

while True:
    pass

# Output:
# signum = 14, frame = <frame object at 0x7fc0c9b010c8>
# signum = 14, frame = <frame object at 0x7fc0c9b010c8>
# signum = 14, frame = <frame object at 0x7fc0c9b010c8>
# signum = 14, frame = <frame object at 0x7fc0c9b010c8>
# signum = 14, frame = <frame object at 0x7fc0c9b010c8>
# signum = 14, frame = <frame object at 0x7fc0c9b010c8>
# signum = 14, frame = <frame object at 0x7fc0c9b010
