import bz2
bz2file = bz2file.BZ2File
from bz2file import compress, decompress

import csv
csv.field_size_limit(sys.maxsize)

import datetime
from datetime import date, timedelta

from dateutil.relativedelta import relativedelta

import glob
import os

from functools import reduce

import gzip
gzipfile = gzip.GzipFile
from gzipfile import compress, decompress

import io
BytesIO = io.BytesIO
StringIO = io.StringIO

import json

import logging

import lxml.etree as etree
from lxml import etree as et

import math

from multiprocessing import cpu_count, Pool

import ntpath

import numpy as np

import pandas as pd

import pyodbc

import re

import requests
from requests import Session
requests = requests.Session()

import requests_cache

import scipy.optimize

import shutil

from six import iteritems, string_types

