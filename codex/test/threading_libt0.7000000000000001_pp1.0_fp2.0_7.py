import threading
threading.stack_size(8388608)

import queue
from queue import Queue

import sys
import socket
import os
import time
import json

from multiprocessing import Process
from multiprocessing import Pipe

from datetime import datetime
from datetime import timedelta

import logging
import logging.handlers

import requests
from requests.exceptions import ConnectionError
from requests.exceptions import ReadTimeout

from pytz import timezone

import traceback

from urllib.parse import urlparse

from market_maker import bitmex
from market_maker.settings import settings
from market_maker.utils import constants, errors, math
from market_maker.utils import log
from market_maker.utils.log import setup_custom_logger

from market_maker.utils.web_socket import BitMEXWebsocket

from market_maker.utils.validation import validate_order

# Used for reloading the bot - saves modified times of key files
import os
