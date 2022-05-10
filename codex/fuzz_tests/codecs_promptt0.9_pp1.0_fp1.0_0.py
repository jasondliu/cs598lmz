import codecs
# Test codecs.register_error('skipfoo',codecs.lookup_error('ignore'))
# codecs.register_error('skipbom',codecs.lookup_error('ignore'))
# codecs.register_error('skipbom2',codecs.lookup_error('ignore'))

# coding: utf-8

import os
import sys
import time
import datetime
import re

debugging = False
verbose = True


def print_if_verbose(message, start_of_line=False):
    if verbose:
        print(message, end='')
        if start_of_line:
            print()


def print_debug(message):
    if debugging:
        print(message, end='')


def print_file_name(filename):
    current_time = time.time()
    # print(' '*(80-len(filename)))
    filename = filename.replace('[', '')
    filename = filename.replace('.', ' ')
    filename = filename.replace(']', '')
    filename = '_
