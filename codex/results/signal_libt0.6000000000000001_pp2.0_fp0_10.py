import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    view = QQuickView()
    url = QUrl('qml/paint_box/main.qml')
    view.setSource(url)
    view.show()
    sys.exit(app.exec_())
