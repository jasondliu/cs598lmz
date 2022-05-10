import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

#import MySQLdb
import pymysql
pymysql.install_as_MySQLdb()

#import MySQLdb.cursors
from django.db import connection

connection.cursor()

#from django.db.backends.mysql.base import DatabaseWrapper
#DatabaseWrapper.data_types['DateTimeField'] = 'datetime'

#from django.core.management.base import BaseCommand, CommandError
#from django.core.exceptions import ObjectDoesNotExist

#from django.conf import settings
#from django.db import connection

#from django.utils import timezone
#from datetime import datetime
#from datetime import timedelta

#import os
#import re
#import sys
#import traceback
#import logging
#import subprocess

#import json

#from datetime import datetime
#from datetime import timedelta

#from django.utils
