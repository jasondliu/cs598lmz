import mmap
import os
import re
import shutil
import signal
import socket
import subprocess
import sys
import tempfile
import threading
import time
import traceback
import unittest
import urllib
import urllib2
import urlparse
import uuid
import warnings

from distutils.version import LooseVersion

from nose.plugins.skip import SkipTest

from pkg_resources import parse_version

from boto.compat import json
from boto.compat.six import BytesIO
from boto.compat.six.moves import http_client
from boto.compat.six.moves.urllib.parse import quote

from boto.connection import AWSAuthConnection
from boto.exception import (
    BotoClientError,
    BotoServerError,
    InvalidUriError,
    S3ResponseError,
    S3CreateError,
    S3DataError,
    S3PermissionsError,
    S3CopyError,
    S3ResponseError,
    S3UploadFailedError,
    S3
