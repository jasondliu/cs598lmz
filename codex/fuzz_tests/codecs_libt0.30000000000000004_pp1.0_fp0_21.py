import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
#import matplotlib.ticker as mticker
#from matplotlib.finance import candlestick_ohlc
#import matplotlib
#import pylab
#matplotlib.rcParams.update({'font.size': 9})

#import numpy as np
#from itertools import count
#import urllib
#import json
#import re
#import datetime as dt
#from time import sleep
#from collections import OrderedDict
#from operator import itemgetter
#import time
#import os.path
#import sys
#import csv
#import glob
#import shutil
#import smtplib
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText
#from email.mime.base import MIMEBase
#from email
