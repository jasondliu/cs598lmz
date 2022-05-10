import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

"""
    This class is to be inherited by other classes,
    it provides the basic functions of a thread class.
    It also provides a start method.
"""
class Threaded(QtCore.QObject):
    def __init__(self, parent=None):
        super(Threaded, self).__init__(parent)
        self.thread = QtCore.QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.start)
        
    def start(self):
        pass
    
    def stop(self):
        self.thread.quit()
        self.thread.wait()
        self.deleteLater()
    
    def run(self):
        pass
        
"""
    This class is used to control the camera.
    It emits the signal newImage when a new image
    is available.
"""
class Camera(Threaded):
    newImage = QtCore.pyqtSignal(QtGui.QImage)
    
