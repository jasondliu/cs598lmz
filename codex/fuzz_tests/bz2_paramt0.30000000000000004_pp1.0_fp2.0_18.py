from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# In[ ]:


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
import time
import json
import requests
import urllib
import logging
import argparse
import datetime
import traceback
import bz2
import gzip
import shutil
import random
import string
import csv
import codecs

from pprint import pprint
from urlparse import urlparse
from urlparse import urljoin
from urlparse import urlsplit
from posixpath import normpath
from bs4 import BeautifulSoup
from collections import OrderedDict

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import No
