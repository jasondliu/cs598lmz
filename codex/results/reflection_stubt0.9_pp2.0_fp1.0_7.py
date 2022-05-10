fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()


def fn1(p):
    pass


def fn2():
    value = 10
    print(dir())
    return value


fn2()


def send_post_to_google_server(req, user_data):
    try:
        server = gevent.spawn(post, "http://www.google.com")
        res = gevent.with_timeout(10, server.get)
        return server.value
    except gevent.Timeout, e:
        print "Timeout posting to google: %s - %s" % (req, user_data)


import time
import threading

class MyThread(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting " + self.name
        # Get lock to synchronize threads
        threadLock.acquire()
        print_time(self.name
