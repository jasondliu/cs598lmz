import sys, threading

def run():
    while True:
        print("Hello, world!")

threading.Thread(target=run).start()
</code>

