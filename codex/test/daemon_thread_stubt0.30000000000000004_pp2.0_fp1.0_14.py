import sys, threading

def run():
    print("Thread started")
    for i in range(0, 100):
        print(i)
    print("Thread finished")

thread = threading.Thread(target=run)
thread.start()

print("Main thread finished")
