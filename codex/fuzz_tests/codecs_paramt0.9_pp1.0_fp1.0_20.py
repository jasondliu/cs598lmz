import codecs
codecs.register_error('strict', codecs.ignore_errors)


from future import standard_library
#from builtins import zip
standard_library.install_aliases()

from PySide import QtCore, QtGui, QtUiTools


def loadUIFile(form_name):
    loader = QtUiTools.QUiLoader()
    ui_file = QtCore.QFile(form_name)
    ui_file.open(QtCore.QFile.ReadOnly)
    ui = loader.load(ui_file)
    ui_file.close()
    return ui

class CountDownButton(QWidget):
    def __init__(self, parent=QApplication.topLevelWidgets()[0],
                 text='CountDown',
                 interval=1,
                 on_finish=None):
        QWidget.__init__(self, parent)
        self.timer = QTimer()
        self.on_finish = on_finish
        self._interval = interval
        self.ui = loadUIFile('countDownButton.ui')
