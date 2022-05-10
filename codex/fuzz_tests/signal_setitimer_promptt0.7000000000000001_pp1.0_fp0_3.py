import signal
# Test signal.setitimer()

def times_up(signum, frame):
    print("times_up called")
    raise TimeoutError("timed out")

def main():
    signal.signal(signal.SIGALRM, times_up)
    signal.setitimer(signal.ITIMER_REAL, 0.1)
    try:
        while True:
            print("Waiting...")
            time.sleep(1)
    except TimeoutError:
        pass
    print("Done")

ma
