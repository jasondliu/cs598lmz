import sys, threading

def run():
    while True:
        print("Hello World")

thread = threading.Thread(target=run)
thread.start()

while True:
    pass
