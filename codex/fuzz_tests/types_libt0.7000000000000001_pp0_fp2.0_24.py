import types
types.ModuleType('pytz')
types.ModuleType('pytz.lazy').tzstr = datetime.datetime.now(pytz.timezone('UTC')).strftime

# Setup Django and Django extensions
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import django
django.setup()

# Import the classes we need
from django.core import management
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connections

from optparse import make_option
import csv
import os
import subprocess

# Connect to the database
connection = connections['etl']
cursor = connection.cursor()

# Create an empty table to store the data
cursor.execute('''DROP TABLE IF EXISTS etl.temp''')
cursor.execute('''CREATE TABLE etl.temp (
	date TIMESTAMP WITH TIME ZONE
