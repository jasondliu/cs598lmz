import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("PokeAssistant")
__version__ = "5.5.0"
__pythonVersion__ = "3.6"

# imports for now
import re
import os
import sys
import json
import argparse
import requests
import threading
import logging
import logging.config
import urllib.parse
import urllib3
from requests.auth import HTTPBasicAuth
from os.path import expanduser
from pkg_resources import resource_string, Requirement
from daemon import runner
from datetime import datetime
from appdirs import user_config_dir

# import extra packages
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()

# create a logger
logger = logging.getLogger()

# update default config
config_dir = user_config_dir('PokeAssistant')
if not os.path.exists(config_dir):
    os.makedirs(config_dir)

# define basic settings
# config
