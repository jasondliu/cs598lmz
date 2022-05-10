import sys, threading

def run():
    for i in range(10000):
        print("Hello World")

t = threading.Thread(target=run)
t.start()

while True:
    pass
