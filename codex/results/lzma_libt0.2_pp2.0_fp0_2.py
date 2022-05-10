import lzma
lzma.open

import os
import sys
import time
import json
import logging
import argparse
import threading
import subprocess
import multiprocessing
import multiprocessing.pool
import multiprocessing.dummy

import requests
import requests.exceptions

import pkg_resources

from . import __version__
from . import __author__
from . import __author_email__
from . import __license__
from . import __url__
from . import __description__
from . import __long_description__
from . import __long_description_content_type__
from . import __keywords__
from . import __classifiers__
from . import __project_urls__
from . import __platforms__
from . import __python_requires__
from . import __install_requires__
from . import __extras_require__
from . import __package_data__
from . import __entry_points__
from . import __zip_safe__
from . import __include_package_data__
from . import __namespace_packages__
from . import __setup_
