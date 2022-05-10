import sys, threading

def run():
    while True:
        print("test")
        time.sleep(3)

thread = threading.Thread(target=run)
thread.start()

while True:
    print("test2")
