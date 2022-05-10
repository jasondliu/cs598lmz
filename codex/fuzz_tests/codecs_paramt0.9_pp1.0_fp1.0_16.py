import codecs
codecs.register_error("replace_but_not_none", codecs.replace_but_not_none)
import glob
import pylab as plt

import matplotlib.ticker as tic
import logging
from IPython import embed

from tqdm import tqdm

from matplotlib.ticker import NullFormatter
nullfmt = NullFormatter()         # no labels

from matplotlib import rcParams

class Correct_for_rabi(object):
	def __init__(self) :
		self.carrier_name = 'smart_10ms_5p5_VCO_carrier_0_VCO_test_0'
		self.acq_time = time.time()

		self.x_label = 'time [ms]'
		self.y_label = 'Atom number'

		self.experiment_name = 'smart_10ms_5p5_VCO_carrier_0_VCO_test_1'
		self.dur_max = 15.
		self.nb_data_points = 100
