import threading
# Test threading daemon

class Worker(threading.Thread):
    def __init__(self, *args, **kwargs):
        self.__timeout = kwargs.pop('timeout', None)
        self.__delayed = kwargs.pop('delayed', None)
        self.__event = kwargs.pop('event', None)
        super(Worker, self).__init__(*args, **kwargs)

    def run(self):
        print "Worker Starting"
        print "Worker Starting #2"
        print "Worker Starting #3"
        if self.__delayed:
            print "Delayed Start"
            self.__event.wait()
        if self.__timeout:
            print "Worker started with timeout %d" % self.__timeout
        else:
            print "Worker started with no timeout"
        print "Worker Exiting"

if __name__ == "__main__":
    t1 = Worker(timeout=1, delayed=True)
    t1.setDaemon(True)
    t1.start()
    t
