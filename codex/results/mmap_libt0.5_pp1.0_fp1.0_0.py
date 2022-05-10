import mmap
import random
import re
import sys
import time

from collections import defaultdict, namedtuple
from datetime import datetime, timedelta
from itertools import islice
from math import ceil, log10
from operator import itemgetter
from os import path
from pprint import pprint
from time import sleep

import numpy as np
import pandas as pd
import requests

from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
from pandas.plotting import register_matplotlib_converters
from pytrends.request import TrendReq

from .utils import (
    _get_df_from_table,
    _get_trends_df,
    _get_trends_df_from_csv,
    _get_trends_df_from_json,
    _get_trends_df_from_json_gz,
    _get_trends_df_from_pickle,
    _get_trends_df_from_url,
    _get
