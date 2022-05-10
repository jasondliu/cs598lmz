import signal
# Test signal.setitimer() --- should simply not hang
if __name__ == '__main__':
    signal.setitimer(signal.ITIMER_REAL, 1)
    signal.pause()
