import threading
# Test threading daemon vs. not daemon

def runInThread(func, *args):
    t = threading.Thread(target=func, args=args)
    t.start()
    print("THREAD:", t, t.isDaemon())
    print(">> T.join()")
    t.join()
    print("THREAD RETURNED:", t)

spinner = threading.Event()
spinner.set()
spin_count = 0
def spin(msg, doneEvent):
    while not doneEvent.isSet():
        sys.stdout.write(msg)
        sys.stdout.flush()


r = random.Random()
r.seed(42)
def randomspin(msg):
    t = threading.current_thread()
    c = 0
    while spinner.isSet():
        i = 0
        s = str(t) + msg + str(i)
        sys.stdout.write(s)
        sys.stdout.flush()
        i = i + 1

        c = c + 1
        if c>1000:
            c
