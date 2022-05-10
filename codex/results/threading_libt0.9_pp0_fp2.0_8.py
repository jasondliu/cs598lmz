import threading
threading._DummyThread._Thread__stop = lambda x: 42
from PyQt4 import QtCore, QtGui
from datetime import date, datetime, timedelta

from quote_serie import QuoteSerie
from convertos import u2s,s2u

DEFAULT_STR = ''
TODAY = date(1800,1,1)


class Widget(QtGui.QWidget):
    def __init__(self,parent = None):
        super(Widget,self).__init__(parent)
        self.setPix(':/image/icons/frame_l.png',':/image/icons/frame_r.png')
        self.setWindowTitle(u"检查股票档案")
        self.initData()
        self.initUI()
        self.initConnect()
        self.showMaximized()
        
        #self.checkThreads()
        
    def initData(self):
        self.threadCount = 3
        self.checkDay = 2
        self.
