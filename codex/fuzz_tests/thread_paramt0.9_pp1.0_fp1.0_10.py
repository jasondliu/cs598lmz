import sys, threading
threading.Thread(target=lambda: sys.stdout.write("t1")).start()
threading.Thread(target=lambda: sys.stdout.write("t2")).start()
print "%%%"
