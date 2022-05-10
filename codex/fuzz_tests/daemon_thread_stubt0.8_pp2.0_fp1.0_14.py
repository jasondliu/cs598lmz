import sys, threading

def run():
    for i in range(0, 100000000):
        print("Hello from a thread!")

t = threading.Thread(target=run)
t.start()
