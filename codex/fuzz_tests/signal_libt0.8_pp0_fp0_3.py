import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    import sys
    import os
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
    sys.path.append(resource_path('lib'))

    from GUI.MainWindow import MainWindow
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()
