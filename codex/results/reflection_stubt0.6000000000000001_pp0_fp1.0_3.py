fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
del fn, gi

# print_function - needed for py2/3 compatibility
from __future__ import print_function

# unicode_literals - needed for py2/3 compatibility
from __future__ import unicode_literals

import argparse
import glob
import os
import sys

# add parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tle import tle

def main():
    # Create the top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    # Create the parser for the "list" command
    list_parser = subparsers.add_parser('list', help='List TLEs')
    list_parser.add_argument('-l', '--long', action='store_true')
    list_parser.add_argument('-v', '--verbose', action='store_true')
   
