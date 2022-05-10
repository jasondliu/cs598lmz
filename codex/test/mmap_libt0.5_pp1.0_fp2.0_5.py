import mmap
import os
import re
import sys
import tempfile

from optparse import OptionParser
from subprocess import Popen, PIPE
from xml.etree import ElementTree


def parse_options():
    parser = OptionParser(usage="usage: %prog [options] <file>")
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose", default=False,
                      help="print all testcases")
    parser.add_option("--gtest_list_tests",
                      action="store_true", dest="list_tests", default=False,
                      help="list all tests")
    parser.add_option("--gtest_filter",
                      action="store", dest="filter", default=None,
                      help="run only matching tests (can be used multiple times)")
    parser.add_option("--gtest_output",
                      action="store", dest="gtest_output", default="xml:report.xml",
                      help="specify output format (default: xml:report.xml)")
    parser.add
