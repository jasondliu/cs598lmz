import threading
# Test threading daemon mode

class MyDaemon(threading.Thread):
    def run(self):
        while True:
            pass

daemon = MyDaemon()
daemon.setDaemon(True)
daemon.start()

daemon.join(2.0)
print daemon.isAlive()

# OUTPUT:
# False
# Daemon thread exiting due to being daemon
# Thread-5:
# Traceback (most recent call last):
#   File "/usr/lib/python2.7/threading.py", line 810, in __bootstrap_inner
#     self.run()
#   File "test_daemon.py", line 9, in run
#     pass
# KeyboardInterrupt
