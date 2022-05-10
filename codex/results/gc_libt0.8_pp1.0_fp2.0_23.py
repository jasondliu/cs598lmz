import gc, weakref
import sys

from PyQt4 import QtCore, QtGui

from gc_widget import Widget
from gc_main_window import Ui_Window

class GUI(Ui_Window):
    def __init__(self):
        Ui_Window.__init__(self)
        self.gc_widgets = []

    def setupUi(self, widget):
        Ui_Window.setupUi(self, widget)

        self.push_btn.clicked.connect(self.push_clicked)
        self.pop_btn.clicked.connect(self.pop_clicked)
        self.pop_all_btn.clicked.connect(self.pop_all_clicked)

    def push_clicked(self):
        w = Widget()
        w.setText("%d" % len(self.gc_widgets))
        self.gc_widgets.append(w)
        self.list_layout.addWidget(w)

    def pop_clicked(self):
        if len(self.gc_wid
