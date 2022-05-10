import mmap
import gzip
import getopt
import sys
import re

def usage():
	print "python " + sys.argv[0] + " [options] -t targetlist.txt -o output.txt"
	print "options:"
	print "-t, --targetlist\tthe list of target proteins"
	print "-o, --output\tthe output path"
	print "-h, --help\tprint help information"

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "ht:o:", ["help", "targetlist=", "output="])
	except getopt.GetoptError:
		usage()
		sys.exit()
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-t", "--targetlist"):
			targetlist = arg
		elif opt in ("-o", "--output"):
			output
