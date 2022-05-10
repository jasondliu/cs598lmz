import select
import signal
import SocketServer
import fcntl
import errno
import time

# from boto.s3.connection import S3Connection
# from boto.s3.key import Key

class BaseRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        cur_pid = os.getpid()
        print 'start %s' % cur_pid
        # self.request.setblocking(1)
        # while True:
        #     time.sleep(1)
        #     print '%s runing' % cur_pid


class ForkingServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
    pass


if __name__ == '__main__':
    # server = ForkingServer(('', 80), BaseRequestHandler)
    # server.serve_forever()

    t = time.time()
    for i in xrange(1, 1000):
        print i
        pid = os.fork()

    print 'use %s' % (time.time() - t)
