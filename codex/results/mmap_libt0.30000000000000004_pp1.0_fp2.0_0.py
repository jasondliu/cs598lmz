import mmap
import os
import re
import sys
import time
import yaml

from collections import OrderedDict
from functools import partial
from itertools import chain
from operator import itemgetter

from . import __version__
from . import __version_info__
from . import __author__
from . import __author_email__
from . import __license__
from . import __url__

from . import config
from . import exceptions
from . import log
from . import utils

from .utils import (
    get_config_path,
    get_config_dir,
    get_config_file,
    get_config_filename,
    get_config_defaults,
    get_config_defaults_path,
    get_config_defaults_dir,
    get_config_defaults_file,
    get_config_defaults_filename,
    get_user_config_path,
    get_user_config_dir,
    get_user_config_file,
    get_user_config_filename,
    get_user_config_
