import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import re
import time
import json
import random
import logging
import argparse
import traceback

from datetime import datetime
from collections import defaultdict

import requests
from requests.exceptions import RequestException

from bs4 import BeautifulSoup

from . import __version__
from . import __author__
from . import __email__
from . import __license__
from . import __copyright__

from . import utils
from . import config
from . import logger
from . import exceptions
from . import constants

from .utils import (
    get_current_time,
    get_random_user_agent,
    get_random_proxy,
    get_random_sleep_time,
    get_random_sleep_interval,
    get_random_sleep_interval_with_jitter,
    get_random_sleep_interval_with_jitter_and_noise,
    get_random_sleep_interval_with_jitter_and_noise_and_
