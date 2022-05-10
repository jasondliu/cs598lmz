import types
types.StringTypes = types.StringType,

import os
import re
import sys
import math
import time
import random
import string
import platform
import cPickle
from ConfigParser import ConfigParser
from cStringIO import StringIO
from collections import deque
from utils import safe_mkdir, boolean
from utils import clean_str_for_filename, clean_str_for_file
from utils import enum, get_current_time
from utils import str_to_int, str_to_float, str_to_bool
from utils import str_from_int, str_from_float, str_from_bool
from utils import get_current_time_str, get_current_timestamp
from utils import get_elapsed_time_str, get_elapsed_time_from_str
from utils import get_short_elapsed_time_from_str, get_short_elapsed_time_str
from utils import get_elapsed_time_from_timestamp, get_elapsed_time_from_double
from utils import get_short_elapsed
