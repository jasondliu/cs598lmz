import weakref
import time
from collections import defaultdict
from itertools import chain, product
from functools import reduce
from operator import mul

from xfel.cxi.cspad_ana.cspad_tbx import dpack, dfiles
from xfel.cxi.cspad_ana.cspad_tbx import iotbx_utils
from six.moves import range

from libtbx import phil as libtbx_phil
from libtbx import easy_mp
from libtbx import slots_getstate_setstate
from dxtbx.model.experiment_list import ExperimentListDumper
#from dxtbx.model.experiment_list import ExperimentListTemplateImporter
from dxtbx.model.experiment_list import ExperimentListFactory
from dxtbx.model.experiment_list import ExperimentList
import dxtbx

from xfel.cxi.cspad_ana.cxi_phil import cxi_version as cxi_phil_version
