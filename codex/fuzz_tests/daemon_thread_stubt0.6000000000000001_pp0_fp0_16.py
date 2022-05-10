import sys, threading

def run():
    while 1:
        time.sleep(1)
        print("New Thread")

thread = threading.Thread(target=run)
thread.start()

while 1:
    time.sleep(1)
    print("Main Thread")
