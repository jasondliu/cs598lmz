import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import sys
import os
import shutil
import time
import re
import csv
import datetime
import zipfile
import subprocess
import logging
import logging.handlers
import logging.config
import traceback
import json
import requests
import socket
import tempfile
import urllib
import urllib2
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.utils import COMMASPACE, formatdate
from email.header import Header

import ConfigParser

reload(sys)
sys.setdefaultencoding('utf-8')

base_path = os.path.dirname(os.path.abspath(__file__))

logging.config.fileConfig(os.path.join(base_path, "logging.conf"))
logger =
