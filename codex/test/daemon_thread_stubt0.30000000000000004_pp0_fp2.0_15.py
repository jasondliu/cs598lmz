import sys, threading

def run():
    while True:
        print("thread running")
        time.sleep(1)

threading.Thread(target=run).start()

while True:
    print("main thread")
