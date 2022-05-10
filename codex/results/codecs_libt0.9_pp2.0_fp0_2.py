import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from dotenv import load_dotenv
load_dotenv()

from models import *

from tools.wechat_4di import *

import datetime
import dateutil.parser
from dateutil import tz
import time
import argparse
from copy import copy
from collections import defaultdict
from pytz import timezone
import json

from sqlalchemy import desc
from sqlalchemy.orm import joinedload
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.expression import false

from tools.data_transfer.push_message_to_wechat import taskLoop
from tools.data_transfer.push_message_to_wechat import individual_task
from tools.data_transfer.push_message_to
