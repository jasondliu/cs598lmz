import threading
# Test threading daemon mode

# non-dameon thread successfull exit, then main program will exit
# daemon will exit when program exit

def f(n):
    print "threading: ", n
    time.sleep(2)
    print "threading end: ", n

t1 = threading.Thread(target=f, args=(1,))
t2 = threading.Thread(target=f, args=(2,))
t1.setDaemon(True)
t1.start()
t2.start()
