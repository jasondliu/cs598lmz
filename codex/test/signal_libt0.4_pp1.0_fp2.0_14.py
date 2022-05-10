import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl

from . import main_window
from . import settings
from . import main_thread
from . import server
from . import client
from . import node
from . import util
from . import log

from . import __version__

def main():
    log.info("Starting version %s" % __version__)
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    main_window.MainWindow(engine)
    settings.Settings(engine)
    main_thread.MainThread(engine)
    server.Server(engine)
    client.Client(engine)
    node.Node(engine)
    util.Util(engine)

    engine.load(QUrl.fromLocalFile("main.qml"))

    sys.exit(app.exec_())
