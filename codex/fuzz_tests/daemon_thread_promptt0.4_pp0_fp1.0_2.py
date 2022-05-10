import threading
# Test threading daemon

def daemon():
    print 'Starting:', threading.currentThread().getName()
    time.sleep(2)
    print 'Exiting :', threading.currentThread().getName()

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print 'Starting:', threading.currentThread().getName()
    print 'Exiting :', threading.currentThread().getName()

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# The daemon thread exits when the program terminates

# The non-daemon thread is still running when the main thread exits, but it is killed when the program terminates

# If you add a time.sleep(1) to the end of the program, the non-daemon thread will exit normally

# If you add a time.sleep(3) to the end of the program, the non-daemon thread will exit
