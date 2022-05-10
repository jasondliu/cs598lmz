import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# import matplotlib
# matplotlib.use('GTK')

import matplotlib.pyplot as plt
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas

import numpy as np
import time

class StatusBar(gtk.Statusbar):

    def __init__(self):
        super(StatusBar, self).__init__()
        self.id = self.get_context_id("StatusBar")
        self.push(self.id, 'Ready')

    def push(self, string):
        super(StatusBar, self).push(self.id, string)

    def pop(self):
        super(StatusBar, self).pop(self.id)

    def set_text(self, string):
        self.pop()
        self.push(string)

class Plotter(gtk.VBox):

    def __init__(self):
        super(Plotter, self).__init__
