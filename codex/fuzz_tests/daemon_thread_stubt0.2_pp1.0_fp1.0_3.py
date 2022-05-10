import sys, threading

def run():
    print("Thread started")
    sys.stdout.flush()
    time.sleep(2)
    print("Thread finished")
    sys.stdout.flush()

t = threading.Thread(target=run)
t.start()

print("Main thread")
sys.stdout.flush()
t.join()
print("Main thread finished")
sys.stdout.flush()
