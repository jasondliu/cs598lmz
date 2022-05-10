import sys, threading

def run():
    while True:
        print("Hello World")

threading.Thread(target=run).start()
</code>
I'm using Python 3.6.5 on Windows 10.

