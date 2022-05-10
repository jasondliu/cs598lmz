import sys, threading

def run():
    print("Thread started")
    for i in range(1, 10):
        print(i)
        time.sleep(1)
    print("Thread finished")

thread = threading.Thread(target=run)
thread.start()

print("Main thread")

while thread.is_alive():
    print("Waiting for thread to finish")
    time.sleep(1)

print("Main thread finished")
