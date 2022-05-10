import codecs
codecs.register_error('strict', codecs.ignore_errors)

import sys
import os
import re
import json
import argparse
import logging
import logging.config
import pkg_resources

from . import __version__
from . import __release__
from . import __copyright__
from . import __description__
from . import __url__
from . import __license__
from . import __keywords__
from . import __author__
from . import __email__
from . import __maintainer__
from . import __maintainer_email__
from . import __package_name__

from . import utils

from . import config
from . import log
from . import cache
from . import database
from . import debug
from . import errors
from . import exceptions
from . import files
from . import log
from . import repository
from . import resources
from . import search
from . import session
from . import settings
from . import user

from . import commands

from . import api

from .database import Database
from .repository import Repository
from .resources import Resource
from
