import types
types.FunctionType = types.BuiltinFunctionType

import unittest
import sys
import os
import re
import subprocess

from rpy2 import robjects
from rpy2.robjects import r
from rpy2.robjects import numpy2ri
from rpy2.robjects import pandas2ri
from rpy2.robjects import conversion
from rpy2.robjects.packages import importr
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage
from rpy2.robjects.packages import DataFrame
from rpy2.robjects.packages import SignatureTranslatedFunction
from rpy2.robjects.packages import SignatureTranslatedFunction
from rpy2.robjects.lib import grid
from rpy2.robjects.lib import grdevices
from rpy2.robjects.lib.dplyr import DataFrame as DplyrDataFrame

from rpy2.rinterface import RRuntimeError
from rpy2.rinterface import Sexp
from rpy2.rinterface import SexpS4


