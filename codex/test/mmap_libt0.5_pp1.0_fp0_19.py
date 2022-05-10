import mmap
import sys
import os
import re
import datetime
from collections import defaultdict
import argparse
import json
from pprint import pprint

#-----------------------------------------------------------------------------------------------------------------------
#- Class
#-----------------------------------------------------------------------------------------------------------------------
class Timer:
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.tstart = datetime.datetime.now()

    def __exit__(self, type, value, traceback):
        if self.name:
            print('[%s]' % self.name),
        print('Elapsed: %s' % (datetime.datetime.now() - self.tstart))


#-----------------------------------------------------------------------------------------------------------------------
#- Functions
#-----------------------------------------------------------------------------------------------------------------------
def parse_args():
    parser = argparse.ArgumentParser(description='Generate an excel file for the given data')
    parser.add_argument('-c', '--config', required=True, help='config file')
