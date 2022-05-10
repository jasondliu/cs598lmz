import sys, threading

def run():
    global stop
    while not stop:
        x=sum(range(10000))   # huidige thread hangen

stop = False
t = threading.Thread(target=run, name="My thread", args=())
t.start()
