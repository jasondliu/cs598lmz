import codecs
codecs.register_error('strict', codecs.ignore_errors)
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlopen
import re
from urllib.parse import urlparse
import os.path
import datetime
from datetime import datetime
from datetime import timedelta
import time
import random
from urllib.error import HTTPError
import os
import sys
import csv
import glob
import json
import requests
from io import BytesIO
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

plt.rcParams['font.family'] = '
