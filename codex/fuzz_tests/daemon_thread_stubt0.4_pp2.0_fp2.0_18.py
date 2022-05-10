import sys, threading

def run():
    while True:
        time.sleep(1)
        print('.', end='')
        sys.stdout.flush()

t = threading.Thread(target=run)
t.start()

while True:
    time.sleep(1)
    print('x', end='')
    sys.stdout.flush()
</code>

