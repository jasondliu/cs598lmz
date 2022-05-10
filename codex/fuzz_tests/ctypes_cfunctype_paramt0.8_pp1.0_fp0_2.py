import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
def call_later(milliseconds, callback):
    if not _main_thread_id:
        raise RuntimeError('QApplication was not created in the main thread.')
    cb_int = int(FUNTYPE(callback)())
    ctypes.pythonapi.PyThreadState_SetAsyncExc(_main_thread_id, ctypes.py_object(SystemExit))

class myThread (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)

    def run(self):
        print "Starting "
        call_later(200, callback)
        print "Exiting"


thread1 = myThread(1)

thread1.start()
</code>
The problem is that the callback function is never called.
Thanks for your help!


A:

After a lot of searchs I found this :
http://eli.thegreenplace.net/2011/04/25/passing-extra-arguments-to-pyqt-slot
It works now, but I don't know why :
<
