import sys, threading

def run():
    while True:
        pass

thread = threading.Thread(target = run)
thread.start()

while True:
    sys.stdout.write('.')
    sys.stdout.flush()
