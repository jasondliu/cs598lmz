import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

#------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------

import sys
import os
import xml.etree.ElementTree as ET
import re
import json
import time

#------------------------------------------------------------------------------
#   Constants
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#   Functions
#------------------------------------------------------------------------------

def print_help():
    print('''
    Usage:
    python3 extract_data_from_xml.py <input_file>

    Example:
    python3 extract_data_from_xml.py C:\\Users\\user\\Desktop\\input.xml
    ''')

def print_header(header):
    print('\n' + '-' * 100)
    print(header)
    print('-' * 100)

def print_footer():
    print('-' * 100)

#------------------------------------------------------------------------------
#   Main
#------------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print_help()
        return
