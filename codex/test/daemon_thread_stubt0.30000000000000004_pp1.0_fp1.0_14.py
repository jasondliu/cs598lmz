import sys, threading

def run():
    while True:
        print("hello")

thread = threading.Thread(target=run)
thread.start()

while True:
    print("world")
