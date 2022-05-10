import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import math

from PySide import QtCore
from PySide import QtGui
from PySide import QtDeclarative

import pyside_util.polygon

#=====================================================================================
class Model():
    def __init__(self):
        self.clear()

    def clear(self):
        self.vertices = []
        self.polygon  = []

    def add_vertex(self, x, y):
        self.vertices.append((x ,y))
        self.polygon  = pyside_util.polygon.convex_hull(self.vertices)

    def remove_last_vertex(self):
        if len(self.vertices) > 0:
            self.vertices.pop()
            self.polygon = pyside_util.polygon.convex_hull(self.vertices)

    def get_vertices(self):
        return self.vertices
