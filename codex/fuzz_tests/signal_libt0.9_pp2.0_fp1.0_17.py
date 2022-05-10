import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PySide import QtCore, QtGui
if not hasattr(QtCore.Qt, 'AA_ShareOpenGLContexts'):
    raise ImportError("Cannot import MagicLeap libraries: Unsupported Qt version")
QtCore.Qt.AA_ShareOpenGLContexts = True

import ml.app
imp.reload(ml.app)

from ml.app import MagicLeapApp

from ml.handcalib import HandCalibWindow

from ml.controller import MyoMainWindow as ControllerMainWindow
from ml.test import ColorControllerMainWindow

from ml.calibrator import HandCalibWorker


if __name__ == '__main__':
    app = MagicLeapApp(sys.argv)
    app.widget = HandCalibWindow()
    app.widget2 = ControllerMainWindow()
    #app.widget2 = ColorControllerMainWindow()

    if len(sys.argv) == 2:
        app.widget.camera_idx = int
