import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:
    sys.stdout.write('\r')
    sys.stdout.flush()
