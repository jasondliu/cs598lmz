import mmap
import re
import robotparser
import StringIO
import subprocess
import sys
import urlparse
import urllib
import urllib2

import wx

def run_dialog(text_ctrl, robot_parser, url, word):
	dialog = wx.TextEntryDialog(None,
		'Enter a word to search for, or a regular expression',
		'Regular Expression Search',
		word)
	if dialog.ShowModal() == wx.ID_OK:
		word = dialog.GetValue().strip()

		if not robot_parser.can_fetch('*', url):
			print "Not allowed to fetch URL %s" % (url)
			return

		try:
			in_file = urllib.urlopen(url)
			in_content = in_file.read()
			in_file.close()

			try:
				pattern = re.compile(word, re.IGNORECASE)
				text_ctrl.Clear()
