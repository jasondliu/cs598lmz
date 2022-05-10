import sys, threading

def run():
    while True:
        print("hello")
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:
    print("world")
    time.sleep(1)
