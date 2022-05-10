import select
import socket
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from lib.core.common import HTTP_DEFAULT_HEADER
from lib.core.common import HTTP_HEADER
from lib.core.common import HTTP_TIMEOUT
from lib.core.common import IS_WIN
from lib.core.common import IS_PYTHON_3
from lib.core.common import MAX_CONNECTION_CHUNK_SIZE
from lib.core.common import MAX_CONNECTION_TOTAL_SIZE
from lib.core.common import readBuffer
from lib.core.convert import hexdecode
from lib.core.convert import utf8encode
from lib.core.data import conf
from lib.core.data import kb
from lib.core.data import logger
from lib.core.enums import CUSTOM_LOGGING
from lib.core.enums import HTTPMETHOD
