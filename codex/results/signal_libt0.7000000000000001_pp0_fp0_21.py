import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import json
import os
import sys
import psycopg2
import psycopg2.extensions
import shutil
import tempfile
import subprocess

from threading import Thread
from pybtex.database import parse_file
from lxml import etree

from . import exceptions as exc


class _Database:
    def __init__(self, config):
        self.config = config
        self.db = None
        self.cursor = None
        self.tx = None
        self.tx_committed = False


    def _connect(self):
        try:
            self.db = psycopg2.connect(**self.config)
            self.db.autocommit = True
            self.cursor = self.db.cursor()
            self.tx_committed = True
        except psycopg2.OperationalError as e:
            raise exc.DatabaseError(e)


    def _close(self):
        if self.db:
            self
