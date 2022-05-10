import io
import json
import csv
import sqlite3
import os
import re
import sys
import shutil
import subprocess
import time
import urllib2
import pickle
import zipfile
import socket
import numpy as np
import progressbar
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count
import tempfile

from collections import Counter 

from bs4 import BeautifulSoup

import pandas as pd
import nltk

import unidecode

import dateutil.parser as dateparser

import graph_tool.all as gt

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

import config
%matplotlib inline
 

def split_text_into_sentences(text):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    raw_sentences = tokenizer.
