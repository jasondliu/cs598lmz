import lzma
lzma.LZMAError

import sys
import os
import time
import datetime
import logging
import tempfile
import shutil
import subprocess

from . import util

log = logging.getLogger('pkginst')

class Package(object):
    def __init__(self, metadata):
        self.metadata = metadata

    def __repr__(self):
        return '<Package %s>' % self.metadata['name']

    def get_metadata(self, key, default=None):
        return self.metadata.get(key, default)

    def get_metadata_list(self, key, default=None):
        return self.metadata.get(key, default) or []

    def get_metadata_dict(self, key, default=None):
        return self.metadata.get(key, default) or {}

    def get_name(self):
        return self.get_metadata('name')

    def get_version(self):
        return self.get_metadata('version')

    def get_description(self):
        return self.get
