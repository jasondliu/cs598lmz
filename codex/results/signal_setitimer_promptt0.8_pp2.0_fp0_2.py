import signal
# Test signal.setitimer() and signal.getitimer()

signal.signal(signal.SIGALRM, alarm_handler)

if __name__ == '__main__':
    delay = 4
    signal.setitimer(signal.ITIMER_REAL, delay, 0)
    print("starting", delay, "second ITIMER_REAL timer")
    while True:
        print("    main: sleeping for 10 seconds")
        time.sleep(10)
        print("    main: sleeping for 10 seconds")
        time.sleep(10)
        print("    main: sleeping for 10 seconds")
        time.sleep(10)
        print("    main: sleeping for 10 seconds")
        time.sleep(10)
        print("    main: sleeping for 10 seconds")
        time.sleep(10)
        print("    main: waking up")
