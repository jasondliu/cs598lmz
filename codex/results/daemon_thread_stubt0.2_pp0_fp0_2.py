import sys, threading

def run():
    while True:
        print("Hello from thread %s" % threading.current_thread())
        sys.stdout.flush()
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:
    print("Hello from thread %s" % threading.current_thread())
    sys.stdout.flush()
    time.sleep(1)
