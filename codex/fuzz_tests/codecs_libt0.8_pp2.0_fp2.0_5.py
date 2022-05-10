import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.indicSoma=QTextCharFormat()
        self.indicSoma.setBackground(QBrush(QColor("yellow")))
        self.indicSoma.setForeground(QBrush(QColor("red")))
        self.indicSoma.setFontUnderline(True)

        self.indicMult=QTextCharFormat()
        self.indicMult.setBackground(QBrush(QColor("green")))
        self.indicMult.setForeground(QBrush(QColor("red")))
        self.indicMult.setFontUnderline(True)

        self.indicDiv=QTextCharFormat()
        self.indicDiv.setBackground(QBrush(QColor("red")))
        self.indicDiv.setForeground(QBr
