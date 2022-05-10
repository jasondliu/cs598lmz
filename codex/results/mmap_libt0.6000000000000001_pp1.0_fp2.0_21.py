import mmap
import re
import locale
import sys
import os
import os.path
import argparse
import functools
import types
import codecs
import collections
import datetime
import time
import csv

from multiprocessing import Process, Queue, Value, Lock
from multiprocessing.managers import SyncManager

from bs4 import BeautifulSoup
from bs4 import UnicodeDammit

import sqlite3
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pyquery import PyQuery as pq

from itertools import izip, count

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize

import htmlentitydefs

import requests
