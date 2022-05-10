import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

class ThreadGrabber(threading.Thread):
    def __init__(self, camera, queue):
        super().__init__()
        self.camera = camera
        # self.queue = queue
        self.running = True
        self.grabbed = False

    def run(self):
        while self.running:
            if self.queue.full():
                continue
            grabbed, frame = self.camera.read()
            if not grabbed:
                break
            self.grabbed = grabbed
            self.queue.put(frame)

class Camera(object):
    def __init__(self, idx):
        self.idx = idx
        self.stop = False
        self.camera = cv2.VideoCapture(self.idx)
        self.queue = Queue()
        self.thread = ThreadGrabber(self.camera, self.queue)

    def start(self):
        self.thread.start()

    def join(self):
        self.thread.running = False
        self.thread.join()

