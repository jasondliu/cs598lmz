import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
import vscode
import os


def main():
    # Populate path for Qt to find QML files
    # This may need to be done elsewhere
    if 'VSCODE_QML_PATH' in os.environ:
        vscode.qml_path = os.environ['VSCODE_QML_PATH']

    os.environ['QT_QUICK_CONTROLS_STYLE'] = 'Material'

    # Initialize Qt stuff
    app = QApplication(sys.argv)
    QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QGuiApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

