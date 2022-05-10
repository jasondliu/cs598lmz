import codecs
codecs.register_error('strict', codecs.ignore_errors)
from datetime import datetime
import datetime
from datetime import date
from pyomo.opt import SolverFactory, SolverStatus, TerminationCondition
from pyomo.opt.dirty import subclass_from_bool
from pyomo.opt.base import Results
from pyomo.opt.blackbox.solve import SolverResults
from lxml import etree
import os
from math import ceil
import platform
from pprint import pprint
import shutil
from time import time
import json

import pyutilib
from pyutilib.common import ApplicationError
import pyutilib.autotest
import pyutilib.autotest.pexpect
import pyutilib.autotest.pexpect_util
from pyutilib.autotest.tests import CAE
import pyutilib.option_parsers
import pyutilib.pyro

from pyomo.common.errors import ApplicationError
from pyomo.common.collections import Options
from pyomo.common.plugin import PluginGlobals
from pyomo.common.solver_capability
