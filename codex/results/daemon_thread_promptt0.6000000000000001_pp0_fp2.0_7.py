import threading
# Test threading daemon

def do_this(what):
    whoami(what)

def whoami(what):
    print("Thread %s says: %s" % (threading.current_thread(), what))

if __name__ == '__main__':
    whoami("I'm the main program")
    for n in range(4):
        p = threading.Thread(target=do_this,
                             args=("I'm function %s" % n,))
        p.start()

# Output:
# Thread <_MainThread(MainThread, started 5992)> says: I'm the main program
# Thread Thread-1(Thread-1, started daemon 5996) says: I'm function 0
# Thread Thread-2(Thread-2, started daemon 5996) says: I'm function 1
# Thread Thread-3(Thread-3, started daemon 5996) says: I'm function 2
# Thread Thread-4(Thread-4, started daemon 5996) says: I'm function 3
# Thread Thread-5(Thread-5, started daemon 5996) says: I'm function 4
#
