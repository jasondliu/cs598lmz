import weakref

from pymt.graphx import drawGraph, drawLabel

class BaseEdge(object):
    def __init__(self, node_from, node_to, **kwargs):
        self.node_from = weakref.ref(node_from)
        self.node_to = weakref.ref(node_to)
        self.color = (1, 1, 1, 1)
        self.width = 1.
        self.arrow = True
        self.label_color = (0, 0, 0, 1)
        self.label = ''
        self.label_dist = 0.5
        self.label_font_size = 8
        self.label_bold = False

        self.node_from().edges_out.append(self)
        self.node_to().edges_in.append(self)

        self.update(**kwargs)

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def draw(self):
        x1, y
