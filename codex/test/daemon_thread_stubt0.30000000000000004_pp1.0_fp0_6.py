import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)

threading.Thread(target=run).start()

while True:
    sys.stdout.write('\r')
    sys.stdout.flush()
