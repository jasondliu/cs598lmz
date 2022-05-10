import signal
# Test signal.setitimer()
def alarm_handler(signum, frame):
    print('Time is up')

def main():
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, 2)
    while True:
        print('Waiting...')
        time.sleep(0.5)

if __name__ == "__main__":
    main()
