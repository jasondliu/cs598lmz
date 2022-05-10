import threading
# Test threading daemon
watcher = [None]
def daemon():
    # This will only run when the main process dies
    print("Starting a daemon thread")
    watcher = threading.current_thread()
    while True:
        print("I'm a daemon!")
        time.sleep(1)

d = threading.Thread(target=daemon)
d.setDaemon(True) # Set this, or the process will hang!
d.start()

while True:
    print("I'm alive!")
    time.sleep(1)
    if not d.isAlive():
        print("The watcher has left")
        break

# Let's use this for forking
def child():
    print("child")
    time.sleep(1)

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print("parent")
            time.sleep(1)

parent()
