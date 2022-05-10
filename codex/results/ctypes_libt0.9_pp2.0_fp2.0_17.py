import ctypes
ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), ctypes.py_object(ctypes.py_object(SystemExit)))
'''
import pyximport
pyximport.install()
import cpy_mpi2_test


class T:

    def __init__(self):

        self.evt = threading.Event()
        self.res = Queue.Queue(10)
        self.stoppers = []
        for i in range(4):
            stopper = threading.Event()
            self.stoppers.append(stopper)
            threading.Thread(target=self._worker, args=(i, stopper)).start()

    def _worker(self, rank, stopper):

        self.evt.set()
        #self.evt.wait()

        no_stopper = True

        while(True):
            self.evt.wait()
            if stopper.is_set():
                print '>'*5 + 'stopping'
                stopper.clear()
                no_
