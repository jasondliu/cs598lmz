import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import logging.handlers
import time
import datetime
import os
import sys
import re
import json
import urllib
import urllib2
import socket
import struct
import binascii
import subprocess
import random
import hashlib
import shutil
import base64
import traceback
import platform
import argparse
import ConfigParser
import math

# TODO:
# - support for multiple servers in config file
# - support for multiple servers in command line arguments
# - support for multiple servers in the UI
# - show server stats in the UI
# - show server stats in the CLI
# - server stats in the db
# - server stats in the API
# - support for multiple clients in the UI
# - support for multiple clients in the CLI
# - support for multiple clients in the API
# - support for multiple clients in the db
# - client stats in the db
# - client stats in the API
# - client stats in the UI
# - client stats in the CLI
# - support for multiple clients in the config file
# - support for multiple clients in the command line arguments

