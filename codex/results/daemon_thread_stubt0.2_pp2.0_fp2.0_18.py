import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:
    print('Hello')
    time.sleep(3)
