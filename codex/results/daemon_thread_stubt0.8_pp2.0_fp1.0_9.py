import sys, threading

def run():
    my_timer = threading.Timer(0, do_work)
    my_timer.start()

def do_work():
    print "hello world"

run()
</code>

