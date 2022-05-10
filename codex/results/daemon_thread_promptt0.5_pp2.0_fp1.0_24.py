import threading
# Test threading daemon
def do_this(what):
    whoami(what)

def whoami(what):
    print("Thread %s says: %s" % (threading.current_thread(), what))

if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = threading.Thread(target=do_this, args=("I'm function %s" % n,))
        p.start()

# Test threading lock
lock = threading.Lock()

def do_this(what):
    whoami(what)

def whoami(what):
    lock.acquire()
    try:
        print("Thread %s says: %s" % (threading.current_thread(), what))
    finally:
        lock.release()

if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = threading.Thread(target=do_this, args=("I'm function %s" % n,))

