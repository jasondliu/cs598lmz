import sys, threading

def run():
    while True:
        print("thread")

thread = threading.Thread(target=run)
thread.start()

while True:
    print("main")
