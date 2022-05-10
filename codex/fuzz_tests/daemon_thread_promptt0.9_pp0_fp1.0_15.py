import threading
# Test threading daemon
# If not daemon, script will not terminate
_daemon = False
# If not daemonized, script will never terminate
_daemon = True

class test_thread(threading.Thread):
    def __init__ (self, name, daemonize):
        threading.Thread.__init__(self, name=name)
        if daemonize:
            self.setDaemon(_daemon)
    def run(self):
       print "%s: %s" % (self.getName(), self.name)

test_thread("test_thread_1", False).start()
test_thread("test_thread_2", True).start()
test_thread("test_thread_3", True).start()

# Test exiting.
# Comment out the below line to see what happens.
exit(0)


# https://docs.python.org/3/library/threading.html

# https://docs.python.org/3/howto/logging.html

# Daemonizing threads/services with PID files
# http://stackoverflow.com/questions/570621
