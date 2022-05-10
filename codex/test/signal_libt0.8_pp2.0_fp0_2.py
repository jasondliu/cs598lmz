import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PySide import QtCore, QtGui
from PySide import QtGui as QtWidgets


class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.table = QtWidgets.QTableWidget(4,4)
        self.button = QtWidgets.QPushButton("remove")
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.remove_row)
        self.setLayout(self.layout)

    def remove_row(self):
        self.table.removeRow(0)

if __name__ == '__main__':
    import sys, os
    app = QtGui.QApplication(sys.argv)
    dia = MyDialog()
