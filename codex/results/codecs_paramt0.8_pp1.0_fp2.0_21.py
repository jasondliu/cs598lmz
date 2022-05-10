import codecs
codecs.register_error("ignore", codecs.lookup_error("ignore"))

import os
import sys

if __name__ == "__main__":
	data = open(sys.argv[1], "r", encoding = "utf-8").read()
	with open(sys.argv[2], "w", encoding = "utf-8") as f:
		f.write("{\n\"" + data + "\"\n}")
