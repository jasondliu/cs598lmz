import sys, threading

def run():
    global x
    while True:
        x = x + 1

x = 0
t = threading.Thread(target=run)
t.start()

