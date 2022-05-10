import sys, threading

def run():
    global t
    t = threading.Timer(10.0, run)
    t.start()
    print "Hello, World!"

run()
</code>

