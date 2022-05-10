import sys, threading

def run():
    sys.stdout.write('\n')
    sys.stdout.flush()
    sys.exit(0)

threading.Timer(1, run).start()

while True:
    sys.stdout.write('\r')
    sys.stdout.flush()
