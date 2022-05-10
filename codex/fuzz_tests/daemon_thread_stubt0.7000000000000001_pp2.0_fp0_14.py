import sys, threading

def run():
    while True:
        print('Thread 1 is running')
        sys.stdout.flush()
        time.sleep(1)

t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

while True:
    print('Main thread is running')
    sys.stdout.flush()
    time.sleep(2)
