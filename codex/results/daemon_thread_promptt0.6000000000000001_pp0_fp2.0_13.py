import threading
# Test threading daemon to allow for timeouts
# This class is meant to be ran as a thread
# It will be able to be killed after a certain amount of time
class Timeout(threading.Thread):
    def __init__(self, time, target=None, args=None, kwargs=None, name=None):
        threading.Thread.__init__(self)
        self.time = time
        if target is not None:
            self.target = target
        if args is not None:
            self.args = args
        if kwargs is not None:
            self.kwargs = kwargs
        if name is not None:
            self.name = name

    def run(self):
        if self.target is not None:
            # Start the thread with the target function passed
            self.target(*self.args, **self.kwargs)
        time.sleep(self.time)

        # If the thread is still alive after the timeout time, kill it
        if self.is_alive():
            print('{} was killed'.format(self.name))
            self.kill
