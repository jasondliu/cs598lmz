import sys, threading

def run():
    print 'hi'
    global timer
    timer = threading.Timer(10.0, run)
    timer.start()

run()
while True:
    pass
