import threading
# Test threading daemon
# https://stackoverflow.com/questions/3788208/python-threading-bug
# https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread-in-python
# https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread-in-python

class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
           
