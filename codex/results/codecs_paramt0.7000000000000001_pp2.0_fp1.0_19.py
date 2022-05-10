import codecs
codecs.register_error("strict", codecs.ignore_errors)

import os
import re
import sys

class App(object):
    def __init__(self, filename, outfile, start, end):
        self.filename = filename
        self.start = start
        self.end = end
        self.outfile = outfile
        self.timelines = []
        self.re_timeline = re.compile("^[ ]+([0-9\.\-]+)[ ]+([0-9\.\-]+)[ ]+([0-9\.\-]+)[ ]+([0-9\.\-]+)[ ]+([0-9\.\-]+)[ ]+([0-9\.\-]+)[ ]+([0-9\.\-]+)[ ]+([0-9\.\-]+)[ ]+([0-9\.\-]+)[ ]+([0-9\.\-]+)")

    def run(self):
        with open(self.filename) as f:
            self.timelines = [line.rstrip() for line in f if self.re_timeline.match(
