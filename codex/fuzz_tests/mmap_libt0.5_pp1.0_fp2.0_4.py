import mmap
import re
import sys

# parse command line options
# -f file
# -s string
# -v verbose
# -d debug
# -h help
# -a all
# -p pattern
#
# --file
# --string
# --verbose
# --debug
# --help
# --all
# --pattern

# parse command line options
# -f file
# -s string
# -v verbose
# -d debug
# -h help
# -a all
# -p pattern
#
# --file
# --string
# --verbose
# --debug
# --help
# --all
# --pattern

def usage():
    print ("""
Usage:
    python3 grep.py [options] pattern [file...]

Options:
    -f, --file=FILE
    -s, --string=STRING
    -v, --verbose
    -d, --debug
    -h, --help
    -a, --all
    -p, --pattern
    """)
    sys.exit(1)

def
