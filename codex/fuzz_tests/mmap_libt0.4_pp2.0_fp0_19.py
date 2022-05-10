import mmap
import sys
import time
import os
import json
import re

from datetime import datetime
from dateutil.parser import parse

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

# Globals
#
ES_HOST = "localhost"
ES_PORT = 9200

# Index names
#
INDEX_NAME = "logstash-%Y.%m.%d"

# The log file to read
#
LOG_FILE = "/var/log/nginx/access.log"

# The pattern to match
#
PATTERN = r'(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http
