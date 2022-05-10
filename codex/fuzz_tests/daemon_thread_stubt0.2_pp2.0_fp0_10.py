import sys, threading

def run():
    print("Thread started")
    for i in range(10):
        print(i)
        time.sleep(1)
    print("Thread finished")

thread = threading.Thread(target=run)
thread.start()

while True:
    print("Main thread")
    time.sleep(1)
    if not thread.is_alive():
        break
