import mmap
import re
import sys
import time
import traceback

from collections import defaultdict
from datetime import datetime

from flask import Flask, jsonify, request

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from log_parser.parser import Parser

app = Flask(__name__)

# TODO: make this configurable
MAX_LOG_SIZE = 1024 * 1024 * 1024

# TODO: make this configurable
LOG_FILE_PATH = '/var/log/nginx/access.log'

# TODO: make this configurable
LOG_FILE_PATH_ERROR = '/var/log/nginx/error.log'

# TODO: make this configurable
LOG_FILE_PATH_ACCESS_SSL = '/var/log/nginx/access_ssl.log'

# TODO: make this configurable
LOG_FILE_PATH_ERROR_SSL = '/var/log/nginx/error_ssl.log'

# TODO: make this
