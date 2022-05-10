import codecs
codecs.register_error('strict', codecs.ignore_errors)

import sys
import os
import re
import time
import datetime
import subprocess
import shutil
import tempfile
import glob
import logging

from xml.dom.minidom import parseString

from . import config
from . import utils
from . import fileutils
from . import log
from . import errors
from . import constants
from . import __version__
from . import __version_info__
from . import __releasedate__
from . import __copyright__
from . import __license__
from . import __author__
from . import __email__
from . import __url__
from . import __downloadurl__
from . import __bugtrack_url__
from . import __description__
from . import __long_description__
from . import __keywords__
from . import __platforms__
from . import __classifiers__
from . import __provides__
from . import __requires__
from . import __obsoletes__
from . import __project_urls__
from . import __entry_points__
from .
