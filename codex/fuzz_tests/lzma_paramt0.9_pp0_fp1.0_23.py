from lzma import LZMADecompressor
LZMADecompressor()
import sys, os
from .zip_buf_sizes.zip_bufsizes import ZIP_CHUNKS
import sys
from bs4 import BeautifulSoup as bs4
from functools import reduce

#log4py modification https://github.com/python-poetry/poetry/issues/1007
from .jar_dependencies import *

def sum_reduce(n1, n2):
    return n1 + n2

def validate_args(args):

    if args.releases and args.snapshots:
        print("{} and {} include each other. Choose one.".format("--releases", "--snapshots"))
        sys.exit(0)
    #     logging.debug("{} and {} include each other. Choose one.".format("--releases", "--snapshots"))
    if args.featured_documents and args.coref_files:
        print("{} and {} include each other. Choose one.".format("--featured_documents", "--coref_files"))
        sys.exit(0)
    #     logging
