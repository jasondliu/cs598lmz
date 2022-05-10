import threading
# Test threading daemon removal
#https://github.com/thinking-in-test/test_threads.py/blob/master/test_threads.py

class ExitThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,  *args, **kwargs):
        """ Init thread. """
        super(ExitThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        """ Stops thread. """
        if self.isAlive():
            self._stop_event.set()

    def stopped(self):
        """ Check for stopping status. Use in loop where required.
            eg.
            if self.stopped():
             self.exit
            """
        return self._stop_event.is_set()

def print_time(delay):
    """ Here is the thread loop. """
    count = 0
    while not exitFlag:
        time.sleep(delay)
       
