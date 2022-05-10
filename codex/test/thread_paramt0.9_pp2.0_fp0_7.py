import sys, threading
threading.Thread(target=lambda: sys.exit()).start()
def timeout():
    # print "timeout"
    sys.exit()            # should fire system exit (5)
Timer(0.01, timeout).start()
while 1:
    pass
