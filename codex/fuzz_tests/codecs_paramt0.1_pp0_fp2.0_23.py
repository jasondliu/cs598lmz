import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import re
import json
import time
import datetime
import logging
import logging.handlers
import traceback
import threading
import subprocess
import signal
import shutil
import tempfile
import urllib
import urllib2
import urlparse
import socket
import random
import hashlib
import base64
import zlib
import binascii
import Queue
import StringIO
import gzip
import ssl
import httplib
import HTMLParser
import cookielib
import xml.dom.minidom
import xml.sax.saxutils
import xml.etree.ElementTree
import xml.etree.cElementTree
import xml.etree.ElementInclude
import xml.etree.ElementPath
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import xml.sax.saxutils as saxutils
import xml.dom.pulldom
import xml.dom.ext
import xml.dom.ext.reader.Sax2
import xml
