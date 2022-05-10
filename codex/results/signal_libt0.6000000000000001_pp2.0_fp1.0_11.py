import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView

if __name__ == '__main__':
    app = QApplication(sys.argv)

    view = QQuickView()
    view.setSource(QUrl('view.qml'))
    if view.status() == QQuickView.Error:
        sys.exit(-1)
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.show()

    sys.exit(app.exec_())
