import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os,sys
sys.path.append(os.path.abspath('../filewalker'))


import filewalker as fw
import fileutils as fu
import utils as u

class File:
    def __init__(self, p):
        self.path = p
        self.ext = fu.get_extension(p)
        self.name = fu.get_filename_without_extension(p)
        self.lines = []
    def read(self):
        self.lines = []
        fu.read_file(self.path, self.lines)
        
class Document:
    def __init__(self):
        self.document = []
        self.cur_file = None
        self.lines = None
        self.offset = 0
        self.length = 0
    def read(self, f):
        self.cur_file = f
        self.cur_file.read()
        self.document = self.cur_file.lines

    def clear(self):
        self.document
