import sys, threading

def run():
    while True:
        print("hello")

threading.Thread(target=run).start()

while True:
    print("world")
