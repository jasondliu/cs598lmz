import sys, threading

def run():
    while True:
        print("hello")
        time.sleep(0.5)

thread = threading.Thread(target=run)
thread.start()

while True:
    print("world")
    time.sleep(0.5)
</code>

