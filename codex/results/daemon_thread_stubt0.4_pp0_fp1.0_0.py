import sys, threading

def run():
    while True:
        print("thread")

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

print("main")

while True:
    pass
