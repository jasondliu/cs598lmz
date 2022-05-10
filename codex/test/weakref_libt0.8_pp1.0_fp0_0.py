import weakref

import numpy as np
import pandas as pd

from test.test_utils import updated_test_file

from csmapi import csmapi, csmutils
from csmapi.csmapi import  CSMError, CSM_RAS_COLUMN, CSM_RAS_PIXEL, CSM_RAS_LINE, CSM_RAS_ROW
from csmapi.model import Model
from csmapi.pvl import Pvl

from csmapi.product_type import ProductType

from csmapi.csm_api_error import *

from csmapi.csm_model_error import *

from csmapi.csm_parser_error import *

import os
import glob
import sys
import copy

_TEST_DIR = os.getcwd()

class TestCsmApi():


    TEST_DATA = os.path.join(_TEST_DIR, "test_files", "test_data")
