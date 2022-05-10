import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import glob
import json
import datetime
import subprocess
import re
import random
import string
import shutil
import logging
import logging.handlers
import time
import smtplib
import socket

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from config import *

# Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Logging to file
log_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
log_file = os.path.join(log
