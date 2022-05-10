import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import logging

from PyQt4 import QtGui, QtCore

from pkg_resources import resource_filename

from openquake.hazardlib.gsim.base import ContextMaker
from openquake.hazardlib import geo
from openquake.commonlib import readinput, logictree, datastore
from openquake.engine import export, logs
from openquake.engine.tools.dem import get_numpy_cache
from openquake.engine.db import models
from openquake.engine.tools.oq_job_supervise import oq_job_supervise
from openquake.engine.utils import config
from openquake.engine.bin import engine
from openquake.engine.bin.engine import (
    get_oqparam, run_calc, run_job, _compose_calc_id)
from openquake.engine.bin.engine import OqParam
from openquake.engine.calculators.
