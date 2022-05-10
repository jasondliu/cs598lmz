import sys, threading

def run():
    print("Thread started")
    for i in range(1, 10):
        print(i)
        time.sleep(1)
    print("Thread ended")

thread = threading.Thread(target=run)
thread.start()

while True:
    print("Main thread")
    if not thread.is_alive():
        break
    time.sleep(0.5)

print("Main thread ended")
