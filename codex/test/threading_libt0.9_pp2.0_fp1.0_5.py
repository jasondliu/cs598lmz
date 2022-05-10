import threading
threading._DummyThread._Thread__stop = lambda x: 42
import orjson
import os
import shutil
import platform
from copy import deepcopy
from fuzzywuzzy import process, fuzz
import email.utils
from datetime import datetime
from mime import MIMEApplication, MIMEAudio, MIMEImage, MIMEMultipart, MIMEText
from email.parser import BytesParser
from email.policy import default
from modules import cache
from time import time
from modules.scraper import scrape
from modules.db import get_cursor, get_db, get_fp_cache
from modules.config import get_config
from modules.errors import return_bad_request, return_not_found, return_error
from modules.utils import redis_status
from pyfingerprint.pyfingerprint import PyFingerprint
from modules.classes.User import User
from modules.classes.Fingerprint import Fingerprint
from modules.classes.Device import Device
from modules.classes import ExpiryUser
from modules.classes.Session import Session
