import gc, weakref
from threading import Thread, Lock

#For supporting Python 3.4 on Pi 3
try:
    import queue
except ImportError:
    # This is here to support python2.7 on a raspberry pi
    import Queue as queue

logger = logging.getLogger(__name__)

lock = Lock()

class Uploader(Thread):
    def __init__(self, queue_size=10, results_queue=None, timestamps=False, compression=5):
        Thread.__init__(self)

        self.queue_size = queue_size
        self.results_queue = results_queue
        self.timestamps = timestamps
        self.compression = compression

        self.stop = False

        self.data_queue = queue.Queue(queue_size)

        self.upload_message = None

    def run(self):


        while not(self.stop):
            try:
                self._upload()
            except Exception as e:
                logger.exception(e)

            time.sleep(30)

        while not(self
