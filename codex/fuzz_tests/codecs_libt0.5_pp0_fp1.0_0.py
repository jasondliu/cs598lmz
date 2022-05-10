import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

from bs4 import BeautifulSoup

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import datetime

from pytz import timezone
import pytz

import logging
import logging.handlers

import os

from pymongo import MongoClient

import re

import time

from pytz import timezone

from PIL import Image

import io

from io import BytesIO

import random

import string

import urllib.request

import sys

from threading import Thread

import multiprocessing

from multiprocessing import Pool

from datetime import datetime

import pandas as pd

import itertools

import math

from multiprocessing import Process

import csv

from openpyxl import Workbook
from openpyxl.
