import sys, threading

def run():
    print("hello")

def run2():
    print("world")

for i in range(10):
    threading.Thread(target=run).start()
    threading.Thread(target=run2).start()
