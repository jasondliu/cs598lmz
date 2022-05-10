import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from collections import defaultdict
import pandas as pd
import numpy as np
import math
import os
import random
import gzip
import ipaddress
import json
import re
import time
import sys
import shutil
import subprocess
import requests
import argparse
import base64
import string
import ftplib

from tqdm import tqdm
import subprocess

from graph import Graph
from email_helper import EmailHelper

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--date', type=str, default=datetime.now().strftime('%Y-%m-%d'), help='date of the data')
parser.add_argument('--duration', type=int, default=14, help='
