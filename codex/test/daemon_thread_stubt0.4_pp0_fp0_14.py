import sys, threading

def run():
    while True:
        print("thread 1")
        sys.stdout.flush()
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:
    print("thread 2")
    sys.stdout.flush()
