import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

while True:
    print("World")
    time.sleep(1)
