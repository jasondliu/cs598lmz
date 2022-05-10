import threading
threading.stack_size(67108864)

from optparse import OptionParser
import sys
import logging
import logging.handlers
import time
import datetime
import os
import platform
import re
import serial
import string
import signal
import traceback
import errno
import json
import csv
import copy
from copy import deepcopy
from collections import defaultdict
import requests

# For MySQL support
try:
	import MySQLdb
	from MySQLdb.cursors import DictCursor
except ImportError:
	pass

# For PostgreSQL support
try:
	import psycopg2
	import psycopg2.extras
except ImportError:
	pass

# For InfluxDB support
try:
	from influxdb import InfluxDBClient
	from influxdb.client import InfluxDBClientError
except ImportError:
	pass

# For MQTT support
try:
	import paho.mqtt.client as mqtt
except ImportError:
	pass

# For Prowl support
