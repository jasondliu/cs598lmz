import codecs
codecs.register_error('strict', codecs.ignore_errors)

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Helvetica', 'Arial']  #, 'Bitstream Vera Sans']
rcParams['font.size'] = 10.
rcParams['contour.negative_linestyle'] = 'solid'

#from coards import from_udunits, to_udunits

from clawpack.visclaw.data import ClawPlotData
from clawpack.visclaw import gaugetools, pylab_util
from clawpack.visclaw.plottools import map_gauges
from clawpack.clawutil.data import ClawData

from setplotfg import setplotfg
from clawpack.amrclaw import geometry
from pathlib import Path

from setplotfg import setplotfg

import numpy as np
import pandas as pd
from scipy.integrate import trapz
from matplotlib.dates import strpdate2num
from datetime import datetime
