import sys, threading

def run():
    print("Thread started")
    while True:
        print("Thread running")
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

while True:
    print("Main thread running")
