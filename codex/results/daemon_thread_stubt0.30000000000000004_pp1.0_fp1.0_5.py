import sys, threading

def run():
    while True:
        print "Hello World"

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

while True:
    pass
