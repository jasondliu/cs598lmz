import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from PySide import QtGui, QtCore
from functools import partial

from view.zombieDisplay import zombieDisplay
from model.characterController import characterController
from model.zController import ZCon
from controller.controller import controller
from view.getName import getName
from model.boardController import boardCont

from model.data import data

from model.data import data


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    # setMain = mainView()
    bC = boardCont()
    bC.setupBoard()


    c = controller()
    # c.setUpTest()

    sys.exit(app.exec_())
