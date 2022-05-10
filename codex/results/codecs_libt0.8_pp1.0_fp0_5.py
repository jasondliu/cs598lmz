import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import logging
logging.basicConfig(filename='/home/rajat/rasp_be/rasp-be/logs/calendar_db.log', level=logging.DEBUG)
import sys
import os
import datetime
import calendar
import time
import uuid
import json
import subprocess
import pandas as pd
import concurrent.futures
import sys
import datetime
from datetime import timedelta
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from firebase_admin import auth
from dateutil import rrule
from dateutil.rrule import *
from dateutil.parser import *
import shutil
import traceback
######################################################################
#config
#staging
#firebase_url="https://raidatabase-dev.firebaseio.com/"
#firebase_storage_url="raidatabase-dev.appspot.com"

