import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys

from PyQt4.QtGui import (QApplication, QFont, QIcon, QMessageBox)

from qgis.core import (QgsApplication, QgsProject)

from mapstory.signals import (setupSignals, cleanupSignals)

from mapstory.gui.mainwindow import MainWindow

def main(argv):
    QgsApplication.setPrefixPath(os.environ["QGIS_PREFIX"], True)
    qgsApp = QgsApplication(argv, True)
    qgsApp.initQgis()

    app = QApplication(argv)
    app.setWindowIcon(QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons", "mapstory.ico")))
    QFont.insertSubstitution(".Lucida Grande UI", "Lucida Grande")
    QFont.insertSubstitution("Lucida Grande", "Lucida Grande")
