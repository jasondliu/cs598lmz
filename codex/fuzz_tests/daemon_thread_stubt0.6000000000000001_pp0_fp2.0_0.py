import sys, threading

def run():
    print "Hello from new thread"

t = threading.Thread(target=run)
t.start()
