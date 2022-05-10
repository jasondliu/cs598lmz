import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) # enable Ctrl+C


import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from PyQt4.QtCore import *
from PyQt4.QtGui import *

from mainwin import Ui_MainWindow
from settings import Ui_Settings
from account import Ui_Account
from nicks import Ui_NickChanger

from auth import Auth
from list import List
from nick import Nick
from search import Search
from conf import Conf
from upload import Upload
from server import Server
from error import Error
from tray import Tray



class Main(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.main = Ui_MainWindow()
        self.main.setupUi(self)

        self.settings = Settings(self)
        self.account = Account(self)
        self.nicks = NickChanger(self)

        self.conf
