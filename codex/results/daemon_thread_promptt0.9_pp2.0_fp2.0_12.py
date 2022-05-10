import threading
# Test threading daemon vs non-dameon behaviour
class Non_Daemon(threading.Thread):
    def run(self):
        while 1:
            pass

d = Non_Daemon(name='non-daemon')
d.start()
d.join(3)
print(d.is_alive())

class Daemon(threading.Thread):
    def run(self):
        pass

d = Daemon(name='daemon')
d.daemon = True
d.start()
d.join(3)

print(d.is_alive())

# Test threading basic locking behaviour
rlock = threading.RLock()
rlock.acquire()
rlock.acquire()
print("Rlock acquired twice")

try:
    rlock.acquire()
except RuntimeError:
    print("Rlock is acquired twice, can't be acquired thrice.")
    
rlock.release()

try:
    rlock.release() 
except RuntimeError:
    print("Rlock is relased twice")

lock = threading.Lock()

