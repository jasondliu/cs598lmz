import threading
# Test threading daemon
# https://docs.python.org/2/library/threading.html
# http://stackoverflow.com/questions/19071512/python-threading-infinite-loop-how-to-stop-it
# http://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread-in-python

class ThreadClass(threading.Thread):
    def run(self):
        while True:
            print "thread"

thread = ThreadClass()
thread.daemon = True
thread.start()

while True:
    time.sleep(1)
    print "main"

# Test threading event
# https://docs.python.org/2/library/threading.html#event-objects
# http://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread-in-python

class ThreadClass(threading.Thread):
    def run(self):
        while True:
            self.event.wait()
            print "
