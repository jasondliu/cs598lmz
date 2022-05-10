import threading
# Test threading daemon
d = threading.Thread(target=daemon, args=('bob',))
d.setDaemon(True)

t = threading.Thread(target=non_daemon, args=('steve',))

d.start()
t.start()

d.join()
t.join()
