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
