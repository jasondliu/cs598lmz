import codecs
codecs.register_error('strict', codecs.ignore_errors)
import numpy as np
import lxml.etree as etree
import time
import inspect
import os
import re
import logging
logging.basicConfig()
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)

global_stamp = ''

def get_stamp():
    global global_stamp
    try:
        return global_stamp
    except NameError:
        global_stamp = '%s' % time.time()
        return global_stamp

class Convert(object):
    def __init__(self,file_name,path=None,force=False):
        self.file_name = file_name
        self.path = path
        self.force = force

    def call_on_subsets(self,subsets=None,subsets_file=None):
        if (subsets is None) and (subsets_file is None):
            raise Exception('subsets or subsets_file parameter should be specified')

        if subsets_file
