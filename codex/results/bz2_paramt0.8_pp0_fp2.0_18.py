from bz2 import BZ2Decompressor
BZ2Decompressor.drain = lambda self: self.decompress('')

import os, sys, re

def get_name(filename):
    return os.path.splitext(filename)[0]

def get_version(filename):
    m = re.search('[0-9]+\.[0-9]+', filename)
    if m:
        return m.group()
    return None

def process(fname):
    name = get_name(fname)
    version = get_version(fname)
    output_fname = name + '.txt'
    print name, version
    f = open(fname, 'r')
    fout = open(output_fname, 'w')
    classname_re = re.compile(r'public class (.*) extends Enum')
    #<T extends Enum<T>>
    enum_value_re = re.compile(r'[    ]+(.*?)\(new .*?, "(.*?)"\)')
    
    try:
        for line in f.readlines():
            m =
