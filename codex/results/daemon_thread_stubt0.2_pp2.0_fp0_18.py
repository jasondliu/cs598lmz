import sys, threading

def run():
    print("Thread started")
    for i in range(1, 100):
        print(i)
    print("Thread ended")

thread = threading.Thread(target=run)
thread.start()

print("Main thread")

# thread.join()

print("Main thread ended")
