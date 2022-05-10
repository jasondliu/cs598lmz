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
