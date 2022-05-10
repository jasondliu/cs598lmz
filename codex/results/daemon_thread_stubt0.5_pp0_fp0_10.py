import sys, threading

def run():
    for i in range(10):
        print("hello")
    sys.stdout.flush()

thread = threading.Thread(target=run)
thread.start()

for i in range(10):
    print("world")
    sys.stdout.flush()

thread.join()

print("thread finished")
sys.stdout.flush()
