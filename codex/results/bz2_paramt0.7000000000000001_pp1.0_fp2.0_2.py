from bz2 import BZ2Decompressor
BZ2Decompressor()

# end of fix

import os
import sys
import time
import json
import random
import requests
import ipaddress
import logging
import argparse
import subprocess
import datetime
import threading
import multiprocessing
import concurrent.futures

from lib.ip_info import IPInfo
from lib.trace_query import TraceQuery
from lib.subprocess_helper import SubprocessHelper

logging.basicConfig(
    format="%(asctime)s %(funcName)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
    stream=sys.stdout,
)

_logger = logging.getLogger("ip_geo_info")


class GeoIPTracer:
    """
    This is the main class that handles the geo-tracing
    """

    def __init__(
        self,
        *,
        ip_list=None,
        ip_file=None,

