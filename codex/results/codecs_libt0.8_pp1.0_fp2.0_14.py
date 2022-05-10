import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import os
import pandas as pd
import pprint
import json
import sys
import csv
import datetime
import time
import numpy as np
import re

import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
pandas2ri.activate()

class RCalculate:
    def __init__(self):

        self.R = robjects.r
        self.R('library("quantmod")')
        self.R('library("TTR")')
        self.R('library("PerformanceAnalytics")')
        self.R('library("xts")')
        self.R('library("lubridate")')
        self.R('library("magrittr")')

        self.R('source("C:/pytest/test3/r
