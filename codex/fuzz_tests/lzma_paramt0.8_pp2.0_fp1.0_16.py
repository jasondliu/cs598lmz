from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self, x: x

import signal, os
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

import urllib.request
opener = urllib.request.build_opener()

def urlopen(url):
	try:
		req = urllib.request.Request(url, method="HEAD")
		url_info = opener.open(req)
		if url_info.code != 200:
			return None
	except Exception as err:
		return None
	return urllib.request.urlopen(urllib.request.Request(url))

def get_input_file():
	import sys
	if len(sys.argv) > 1:
		input_file = sys.argv[1]
	else:
		input_file = "-"
	if input_file == "-":
		input_stream = sys.stdin.buffer
		if hasattr(sys.stdin, "isatty") and sys.stdin.
