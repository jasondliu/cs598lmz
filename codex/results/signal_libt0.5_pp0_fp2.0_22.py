import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QObject, QUrl, pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine

from qt_gui.model import Model
from qt_gui.controller import Controller
from qt_gui.qml_bridge import QmlBridge

from qt_gui.qml_bridge import QmlBridge
from qt_gui.controller import Controller
from qt_gui.model import Model
from qt_gui.view import View

if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Create an instance of the model
    model = Model()

    # Create QmlBridge instance
    qml_bridge = QmlBridge(model)

    # Create an instance of the controller
    controller = Controller(model, qml_bridge)

    # Create an instance of the view
