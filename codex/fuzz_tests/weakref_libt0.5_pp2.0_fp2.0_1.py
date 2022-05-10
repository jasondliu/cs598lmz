import weakref

from PyQt5.QtCore import QObject, QTimer, pyqtSignal


class Timer(QObject):
    """
    A timer to call a function periodically.

    This is a Qt implementation of the :class:`Timer` class.

    Parameters
    ----------
    interval : float
        The interval in seconds.
    callback : callable
        The function to call.
    oneshot : bool
        If True, the timer stops after the first call.

    """
    def __init__(self, interval, callback, oneshot=False):
        super().__init__()
        self.interval = interval
        self.callback = callback
        self.oneshot = oneshot
        self.timer = QTimer()
        self.timer.setInterval(interval * 1000)
        self.timer.timeout.connect(self._call_callback)
        self.timer.setSingleShot(oneshot)

    def start(self):
        """
        Start the timer.
        """
        self.timer.start()

    def stop(self):
        """
