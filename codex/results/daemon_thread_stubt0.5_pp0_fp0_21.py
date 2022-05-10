import sys, threading

def run():
    while True:
        print("hello")
        time.sleep(1)

threading.Thread(target=run).start()

while True:
    print("world")
    time.sleep(1)
</code>

