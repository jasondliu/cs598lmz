import select
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import traceback
from unittest import SkipTest, TestCase

try:
    from unittest.mock import Mock
except ImportError:
    from mock import Mock

from . import __version__


DEF_TIMEOUT = None
DEF_SERVER_ADDR = ('127.0.0.1', 0)

# Try the fastest, most secure ciphers first
_ciphers = (
    'EECDH+ECDSA+AESGCM EECDH+aRSA+AESGCM EECDH+ECDSA+SHA384 EECDH+ECDSA+SHA256 EECDH+aRSA+SHA384 EECDH+aRSA+SHA256'
    ' EECDH+aRSA+RC4 EECDH EDH+aRSA RC4 !aNULL !eNULL !LOW !3DES !MD5 !EXP !PSK !SRP !DSS'
)

