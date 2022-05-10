import sys, threading

def run():
    while True:
        print("Hello")

threading.Thread(target=run).start()

print("Hello")
</code>

