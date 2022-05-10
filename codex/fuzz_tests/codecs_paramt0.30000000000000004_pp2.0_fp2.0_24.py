import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import re

def get_file_contents(filename):
    with open(filename, 'r') as f:
        return f.read()

def get_file_lines(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def get_file_lines_as_list(filename):
    with open(filename, 'r') as f:
        return list(f)

def get_file_lines_as_list_strip(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def get_file_lines_as_list_strip_filter(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def get_file_lines_as_list_strip_filter_ignore_comments(filename):
    with open(filename, 'r') as f:
        return [line.strip
