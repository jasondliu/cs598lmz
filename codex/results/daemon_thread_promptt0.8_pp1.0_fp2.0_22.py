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
        

# threading.enumerate()
# threading.current_thread()
# threading.active_count()

# Test threading lock:
# Test threading daemons:
print(threading.active_count())
print(threading.enumerate())
print(threading.current_thread())
