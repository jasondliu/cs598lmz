import codecs
codecs.register_error('replace_cyrillic', codecs.replace_errors( 'replace_by' ))

import datetime
import re
from pprint import pprint
import math, sys, os
#from math import log
from bitarray import bitarray
from collections import namedtuple

from index_common import *
#from pyudmf import *

QueryResult = namedtuple('QueryResult', 'doc_id freq')

index = Index()
def main(index_dir, query_file, results_file, udmftree):
    """
    """

    index.load(index_dir, 'index_i.dat', 'df')
    pprint(index.df)

    #udmftree = UDMFTree()
    #udmftree.from_file(os.path.join(index_dir, 'UDMF_tree.udmf'))

    #with codecs.open(query_file, 'r', 'cp1251', errors='replace_cyrillic') as f:
    #    for query in f:

    with open(query_file,
