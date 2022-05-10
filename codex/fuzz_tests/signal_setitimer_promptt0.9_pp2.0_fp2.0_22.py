import signal
# Test signal.setitimer throws NotImplementedError
try:
    signal.setitimer(*(signal.ITIMER_REAL,)*2)
except NotImplementedError:
    print("SKIP")
    raise SystemExit

def handler(signum, frame):
    print("get", signum)
    raise SystemExit

signal.signal(signal.SIGALRM, handler)

def main():
    signal.setitimer(signal.ITIMER_REAL, 1, 0)
    while True:
        pass

main()
