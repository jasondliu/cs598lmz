import sys, threading

def run():
    print("Thread started")
    for i in range(10):
        print(i)
        time.sleep(1)
    print("Thread ended")

thread = threading.Thread(target=run)
thread.start()

print("Main thread")

for i in range(10):
    print(i)
    time.sleep(1)

print("Main thread ended")
