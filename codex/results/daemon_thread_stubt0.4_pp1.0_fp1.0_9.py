import sys, threading

def run():
    while True:
        print("Hello, world!")
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

while True:
    print("Hello, main!")
    time.sleep(1)
