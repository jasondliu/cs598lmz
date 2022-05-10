import weakref

from PyQt5.QtCore import QObject, pyqtSignal

from .. import signals


class BaseJob(QObject):
    """
    Base class for all jobs
    """
    sigFinished = pyqtSignal(object)
    sigFailed = pyqtSignal(object)
    sigCanceled = pyqtSignal(object)

    def __init__(self):
        QObject.__init__(self)
        self._canceled = False
        self._failed = False
        self._finished = False
        self.sigFinished.connect(self._onFinished)
        self.sigFailed.connect(self._onFailed)
        self.sigCanceled.connect(self._onCanceled)

    def start(self):
        """
        Start the job
        """
        raise NotImplementedError

    def cancel(self):
        """
        Cancel the job
        """
        self._canceled = True
        self.sigCanceled.emit(self)

    def fail
