import threading
# Test threading daemon mode.


def daemon():
    print("Daemon started")
    i = 0
    while True:
        sys.stdout.write("Daemon Alive! %s (%i)\n" % (threading.currentThread().getName(), i))
        sys.stdout.flush()
        time.sleep(5)
        i += 1


def non_daemon():
    print("Non daemon started")
    i = 0
    # time.sleep(100000)
    while True:
        sys.stdout.write("Non-daemon Alive! %s (%i)\n" % (threading.currentThread().getName(), i))
        sys.stdout.flush()
        time.sleep(5)
        i += 1


# Start a thread with the daemon flag set.
d = threading.Thread(name="daemon", target=daemon)
d.setDaemon(True)

# Start a non-daemonic thread.
t = threading.Thread(name="non-daemon", target=non_daemon)

# Wait until the daemon thread exits, e
