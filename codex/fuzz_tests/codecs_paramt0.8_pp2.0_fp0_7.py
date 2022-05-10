import codecs
codecs.register_error('replace_py3k', codecs.lookup_error('replace'))
import numpy as np

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def load_file(f):
    """
    Load file content
    """
    with open(f, "r") as fh:
        return fh.readlines()

def load_file_raw(f):
    """
    Load file content (without EOL)
    """
    with open(f, "r") as fh:
        return fh.read()

def write_line(outpath, line):
    """
    Write line to a file
    """
    with open(outpath, "a") as fh:
        fh.write(line+"\n")

def write_lines(outpath, lines):
    """
    Write lines to a file
    """
    with open(outpath, "a") as fh:
        fh.write("".join([ l+"\n" for l in lines ]))

def
