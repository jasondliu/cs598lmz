import threading
# Test threading daemon
def daemon():
    print("starting daemon")
    time.sleep(2)
    print("daemon closing")


def non_daemon():
    print("non daemon starting")
    time.sleep(1)
    print("non daemon closing")

d = threading.Thread(name="daemon", target=daemon)
d.setDaemon(True)

t = threading.Thread(name="non daemon", target=non_daemon)

d.start()
t.start()

d.join()
t.join()

print("done")
