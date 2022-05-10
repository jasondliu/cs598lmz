import lzma
# Test LZMADecompressor based stream to decompress lzma format file
from gzip import GzipFile
import os
import sys
import json
from datetime import date
import traceback
import logging
import re
import psycopg2

class IPPrefixDB(object):
    """
    Class IPPrefixDB used to store ip prefix in form (network,cidr)
    """
    ni = re.compile(r'''^(\d+)\.(\d+)\.(\d+)\.(\d+)$''')

    def __init__(self):
        #self.logger = logging.getLogger(__name__)
        self.ip_prefixes = []

    def load_csv(self, fi):
        """
        Read ip prefix from CSV file
        :param fi: name of input file
        """
        #self.logger.debug('starting loading ip prefix list from: %r', fi)
        with open(fi, 'r') as ifh:
            for il in ifh:
                self.ip_prefixes.append(tuple(il.strip().split(
