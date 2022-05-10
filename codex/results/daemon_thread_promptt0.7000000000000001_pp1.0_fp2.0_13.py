import threading
# Test threading daemon
import time
import unittest
# Test threading
import os
import sys
import subprocess
import signal
import zipfile
import shutil
import StringIO
import re
import filecmp
import json
import atexit
import socket
import urllib2
import hashlib
import random
import stat
import errno

#TODO: Split into multiple tests
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        # Test pid file
        cls.pidFilePath = os.path.join(tempfile.gettempdir(), 'test_pid_file.pid')
        cls.pidFile = open(cls.pidFilePath, 'w')

        # Test log file
        cls.logFilePath = os.path.join(tempfile.gettempdir(), 'test_log_file.log')
        cls.logFile = open(cls.logFilePath, 'w')

        # Test temp file
        cls.tempFilePath = os.path
