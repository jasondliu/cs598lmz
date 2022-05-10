import weakref

class ReplyObj(object):
    def __init__(self, fd, timeout, msgid, cb, obj, meth, wait_cls):
        self.fd = fd
        self.timeout = timeout
        self.msgid = msgid
        self.cb = weakref.ref(cb)
        self.obj = obj
        self.meth = meth

        self.wait_cls = wait_cls
        self.lock = self.wait_cls.create_lock()

        #weakref.proxy(logging.getLogger(), self.retransmit)

    #def retransmit(self):
    #    pass

    def run(self, conn, seq):
        if self.cb() is not None:
            self.meth(self.obj, conn, seq)
            self.lock.acquire()
            try:
                self.lock.notifyAll()
            finally:
                self.lock.release()

    def wait(self):
        self.lock.acquire()
