import sys, threading

def run():
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdin.readline()

threading.Thread(target=run).start()

import time

while True:
    time.sleep(1)
    sys.stdout.write("\r" + str(time.time()))
    sys.stdout.flush()
