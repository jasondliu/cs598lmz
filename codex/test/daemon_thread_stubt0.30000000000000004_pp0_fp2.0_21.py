import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

while True:
    sys.stdout.write('\r')
    sys.stdout.flush()
