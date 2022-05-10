import sys, threading

def run():
    print("Thread started")
    for i in range(1, 100):
        print(i)
        time.sleep(0.1)
    print("Thread ended")

thread = threading.Thread(target=run)
thread.start()

print("Main thread ended")
