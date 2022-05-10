import threading
# Test threading daemon
import time

def daemon():
    print('Asked for daemon thread')
    time.sleep(100)
    print('100 seconds later')

#d = threading.Thread(name='daemon', target=daemon)
#d.setDaemon(True)

#d.start()

#time.sleep(1)

# assert that the thread is a daemon
#assert d.isDaemon() is True
#assert t.isDaemon() is False

# 10 seconds later, no daemon thread alive
#time.sleep(10)

# Daemon threads are terminated automatically when the main thread ends
#assert d.isAlive() is False

# Daemon threads are terminated when the main thread ends.
#assert t.isAlive() is True
#assert t.is_alive() is True

#t.join()


# A single thread
def a(name, counter):
    time.sleep(1)
    print('Hello', name, counter)
    time.sleep(1)
    print('Bye', name, counter)

#a('Bob
