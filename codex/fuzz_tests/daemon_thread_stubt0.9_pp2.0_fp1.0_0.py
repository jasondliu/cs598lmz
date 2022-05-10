import sys, threading

def run():
    n = 0
    for i in range(1000):
        n += 1
        print sys.argv[1], ':', `n`
        threading._sleep(0.1)
"""))

class threading_test_QQQQ(unittest.Thread):

    def __init__(self):
        unittest.Thread.__init__(self)
        self.setDaemon(True)
        self.finished = False
        self.running = False

    def start(self):
        self.__running = True
        unittest.Thread.start(self)

    def run(self):
        self.__running = True
        try:
            execfile(TESTFN, {'__name__' : '__main__'})
        finally:
            self.__running = False
            self.__finished = True

    def isAlive(self):
        return self.__running

    def isFinished(self):
        return self.__finished

class ThreadRunningTests(unittest.TestCase):

    def test_var
