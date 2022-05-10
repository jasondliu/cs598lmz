import threading
# Test threading daemon
import urllib.request
import urllib.parse
import urllib.error

import serial
import serial.threaded

import lib.config

class TestThread(threading.Thread):
    def __init__(self, threadID, name, counter, delay=1):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.delay = delay
        self.exitFlag = False
        self.runFlag = False

    def run(self):
        print ("Starting " + self.name)
        print_time(self.name, self.counter, self.delay)
        print ("Exiting " + self.name)

    def print_time(threadName, counter, delay):
        while counter:
            if self.exitFlag:
                threadName.exit()
            time.sleep(delay)
            print ("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1
        """
        while not self.
