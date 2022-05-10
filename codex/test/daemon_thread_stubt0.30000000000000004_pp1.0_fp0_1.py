import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        time.sleep(0.1)

t = threading.Thread(target=run)
t.daemon = True
t.start()

while True:
    sys.stdout.write('o')
