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
