import sys, threading

def run():
    while True:
        print("Hello World")
        time.sleep(0.5)

thread = threading.Thread(target=run)
thread.start()

while True:
    pass
