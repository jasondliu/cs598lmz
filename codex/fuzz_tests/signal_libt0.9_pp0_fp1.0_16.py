import signal
signal.signal(signal.SIGINT, singal.SIG_DFL)

import os
from collections import OrderedDict
os.environ['PYTHONINSPECT'] = 'True'
from matplotlib import use
use('Qt4Agg')

from PyQt4 import QtGui
from PyQt4.QtCore import QThread, pyqtSignal
from pylab import rcParams
from ImagingReso.fitter.doctor import Doctor
from ImagingReso.resonance import Gaussian2D, Fano2D
from ImagingReso.resonance import GaussianIH
from ImagingReso.fitter.analyzer import get_fit_parameters, Axis
from ImagingReso.fitter.mpl_widget import MplWidget

from ms_deisotope.deconvolution import Deconvoluter, PeakReshaper, BunchFitter
from ms_deisotope.peak_set import DeconvolutedPeak, DeconvolutedPeakSet
from ms_deisotope.peak_set import Mass
