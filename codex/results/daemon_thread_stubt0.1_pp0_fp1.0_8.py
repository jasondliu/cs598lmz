import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

threading.Thread(target=run).start()

while True:
    print("World")
    time.sleep(1)
</code>

