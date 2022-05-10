import mmap
import os
import re
import sys
import time

from collections import defaultdict
from datetime import datetime
from itertools import chain
from optparse import OptionParser
from os.path import dirname, join, realpath
from subprocess import Popen, PIPE
from threading import Thread

from lib.config import Config
from lib.logger import Logger
from lib.utils import get_file_content, get_file_size, get_file_sha1, get_file_sha256, get_file_sha512, get_file_ssdeep, get_file_type, get_file_yara, get_file_magic, get_file_entropy, get_file_mime, get_file_mime_type, get_file_mime_encoding, get_file_mime_string, get_file_mime_string_encoding, get_file_mime_string_extension, get_file_mime_string_short, get_file_mime_string_short_extension, get_file_mime_string_long, get
