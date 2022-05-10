import sys, threading

def run():
    print 'test'
    threading.Timer(1.0, run).start()

run()
while True:
    pass
