from lzma import LZMADecompressor
LZMADecompressor()
import os, sys, stat, re, fnmatch, time, random,  getpass , optparse , sqlite3
from subprocess import Popen, PIPE, STDOUT, call

def get_all_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def get_all_files(a_dir,suffix):
    return [name for name in os.listdir(a_dir)
            if not os.path.isdir(os.path.join(a_dir, name)) and name.endswith(suffix)]


def getcontent(filename):
    with open(filename, 'r') as f:
        return f.read()

def writefile(filename,content):
    content = content.replace('\r','')
    f = open(filename,"w")
    f.write(content)
    f.close()

def generate_query_list(db_filename, min_time
