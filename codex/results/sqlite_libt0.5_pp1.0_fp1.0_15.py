import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import datetime
import json
import logging
import socket
import random
import urllib.request
import urllib.parse
import urllib.error
import ssl
import traceback
import getpass
import re
import base64
import hashlib
import platform
import subprocess
import pwd
import grp
import stat
import tempfile
import shutil
import copy
import textwrap
import locale
import argparse
import configparser
import ast
import pkg_resources

# Global variables

version = "0.83.6"

# The following are used to set the default values for the configuration file
# and command line options.

default_config_file = os.path.join(os.path.expanduser("~"), ".config", "indicator-multiload.conf")
default_config = {
    "general": {
        "show_icons": True,
        "show_text": True,
        "show_tooltips": True,
        "show_graph": True,
        "graph_width": 100
