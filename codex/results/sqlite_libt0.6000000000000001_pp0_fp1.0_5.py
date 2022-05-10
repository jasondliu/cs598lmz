import ctypes
import ctypes.util
import threading
import sqlite3
import os
import os.path
import sys
import argparse
import logging
import time
import subprocess
import shutil
import random
import json
import re
import datetime
import traceback
import hashlib

from . import __version__
from . import config
from . import util
from . import web
from . import runner
from . import db
from . import logs
from . import status
from . import mime
from . import dns

__all__ = ["init", "start", "stop", "restart", "run"]

log = None

def init(args):
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    log = logging.getLogger('httpolice')

    if args.version:
        print(__version__)
        return 0

    if args.config:
        config.load(args.config)

    if args.logs:
        logs.setup(args.logs)

    if args.dns:
