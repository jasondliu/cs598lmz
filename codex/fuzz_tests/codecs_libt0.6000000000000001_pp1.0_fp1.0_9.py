import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import csv
import ctypes
import datetime
import os
import os.path
import re
import subprocess
import sys
import time
import urllib
import urllib2
import zipfile

import BeautifulSoup

def main():
	if len(sys.argv) < 2:
		print 'Command line usage: python %s [date] [url]' % os.path.basename(sys.argv[0])
		print '  date: YYYY-MM-DD format'
		print '  url: optional, use if you want to override the URL used to get the data'
		sys.exit(1)

	date = sys.argv[1]
	url = 'http://www.census.gov/foreign-trade/Press-Release/current_press_release/exh1.txt'
	if len(sys.argv) > 2:
		url = sys.argv[2]

	#
