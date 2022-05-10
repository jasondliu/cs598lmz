import mmap
import os
import re
import time
import traceback
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from threading import Thread

import click
import requests
import yaml
from bs4 import BeautifulSoup
from clickclick import AliasedGroup
from clickclick.console import print_table
from tabulate import tabulate

from . import __version__
from .config import Config
from .dns import DNS
from .exceptions import (
    AccountNotFound,
    AccountNotLoggedIn,
    AccountNotVerified,
    CloudflareError,
    InvalidEmailError,
    InvalidZoneNameError,
    MissingCredentials,
    MissingRecords,
    RateLimitError,
    TimeoutError,
    ZoneNotFound,
)
from .utils import (
    get_zone_id,
    get_zone_name,
    get_zone_names,
    is_ip,
    is_ip_valid,
    is_ipv4,
    is_ipv6,
    is_
