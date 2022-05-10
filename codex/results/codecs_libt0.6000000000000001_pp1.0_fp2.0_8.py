import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import csv
from datetime import datetime
from datetime import timedelta
import json
import logging
from operator import itemgetter
import os
import pandas as pd
import psycopg2
from psycopg2 import sql
import re
from shutil import copyfile
import signal
from subprocess import Popen, PIPE
from subprocess import call
import sys
from time import time
import traceback

from utils import (create_logger,
                   debug,
                   eprint,
                   info,
                   warning)
from etl_db import (postgres_db,
                    postgres_schema,
                    postgres_user,
                    postgres_password)

from etl_activity_log import (activity_log_insert,
                              activity_log_update,
                              activity_log_success)
from etl_audit_log import (audit_log_insert,
                           audit_log_update,
                           audit_
