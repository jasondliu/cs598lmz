import sys, threading

def run():
    while True:
        print("Hello")

t = threading.Thread(target=run)
t.daemon = True
t.start()

while True:
    print("World")
