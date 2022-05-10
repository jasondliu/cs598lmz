import socket
import sys
import threading
import time

LOG_FORMAT = '%(asctime)s %(message)s'

if os.path.exists('/tmp/testlog.log'):
    os.remove('/tmp/testlog.log')

logging.basicConfig(
    filename='/tmp/testlog.log',
    level=logging.DEBUG,
    format=LOG_FORMAT,
    filemode='w'
)


class MyThread(threading.Thread):
    def __init__(self, event=None, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self.event = event

    def run(self):
        logging.debug("%s started" % self.getName())
        if self.event:
            while not self.event.isSet():
                time.sleep(1)
        logging.debug("%s ended" % self.getName())


lock = threading.Lock()


def worker():
    with lock:
        print
