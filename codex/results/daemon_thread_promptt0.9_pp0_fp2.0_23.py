import threading
# Test threading daemon mode.

def daemon():
    print 'start'
    #print(threading.currentThread().getName())
    time.sleep(3)
    print 'end'

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True) # once this is set, it cannot be overriden.

d.start()
d.join() 
#Calling isAlive() will tell you whether the thread is still running. (not started or stopped?)
d.isAlive()

##

# Treading event 
# A threading.Event object manages an internal flag that can be set to true with the set() method and reset to false with the clear() method. 
# The wait() method blocks until the flag is true.

def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    print('wait_for_event starting')
    print(threading.currentThread().getName(), 'Starting')
    event_is_set = e.wait()
    print(threading.currentThread().get
