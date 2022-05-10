import weakref

from PyQt5 import QtGui, QtCore, QtWidgets

from .board import Board


class Game(QtWidgets.QGraphicsView):
    def __init__(self, width, height):
        super(Game, self).__init__()
        self.setDragMode(1)
        self.width, self.height = width, height
        self.board = Board(self.width, self.height)
        self.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.scene = QtWidgets.QGraphicsScene(0, 0,
                                              (width-1)*self.board.cell_width,
                                              (height-1)*self.board.cell_width)
        self.scene.addItem(self.board)
        self.setScene(self.scene)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QPixmap('img/bg.png')))
