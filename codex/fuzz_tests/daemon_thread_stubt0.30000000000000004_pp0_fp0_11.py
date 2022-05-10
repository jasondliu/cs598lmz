import sys, threading

def run():
    print("Thread started")
    for i in range(1000000):
        pass
    print("Thread ended")

thread = threading.Thread(target=run)
thread.start()

print("Main thread")

while thread.is_alive():
    pass

print("Main thread ended")
