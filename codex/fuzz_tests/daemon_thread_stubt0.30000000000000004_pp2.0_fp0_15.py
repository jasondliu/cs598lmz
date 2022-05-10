import sys, threading

def run():
    while True:
        print("Hello")

thread = threading.Thread(target=run)
thread.start()

while True:
    print("World")
</code>

