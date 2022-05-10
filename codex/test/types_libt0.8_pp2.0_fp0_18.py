import types
types.ModuleType.__repr__ = lambda self: ''

import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import pyplot as plt
from matplotlib.patches import Patch
import numpy as np

from sklearn import metrics

from scipy import stats
import scipy

class Plotter(object):
    def __init__(self, name, model_names, output_dir):
        self.name = name
        self.model_names = model_names
        self.output_dir = output_dir

    def get_filename(self):
        return os.path.join(self.output_dir, self.name)

    def save(self):
        pdf_filename = "{0}.pdf".format(self.get_filename())
        print('Creating file {0}...'.format(pdf_filename))
        with PdfPages(pdf_filename) as pdf:
            self.plot(pdf)
