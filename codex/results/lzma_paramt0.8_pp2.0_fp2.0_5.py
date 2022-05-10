from lzma import LZMADecompressor
LZMADecompressor()

import hashlib

import json
import pprint
pp = pprint.PrettyPrinter(indent=2)

# import gzip
import os
import random
import shutil
import sys
import tempfile

from urllib.request import urlopen, Request

import zipfile


class IndexInfo:
    def __init__(self, **kwargs):
        self.index_name = kwargs.get('index_name')
        self.index_number = kwargs.get('index_number')
        self.index_url = kwargs.get('index_url')
        self.index_hash_url = kwargs.get('index_hash_url')
        self.index_archive_hash = kwargs.get('index_archive_hash')

    def __repr__(self):
        return str(
            (
                self.index_name,
                self.index_number,
                self.index_url,
                self.index_hash_url,
                self.index_archive_hash
            )
        )



