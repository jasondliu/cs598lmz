import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

# https://stackoverflow.com/questions/1408356/keyboard-interrupts-with-pythons-multiprocessing-pool
# https://stackoverflow.com/questions/11312525/catch-ctrlc-sigint-and-exit-multiprocesses-gracefully-in-python

import multiprocessing
import signal
import sys

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, handler)
    pool = multiprocessing.Pool(processes=4)
    while True:
        pool.apply_async(long_running_job)

if __name__ == '__main__':
    main()

# https://stackoverflow.com/questions/11312525/catch-ctrlc-sigint-and-exit-multiprocesses-gracefully-in-python
