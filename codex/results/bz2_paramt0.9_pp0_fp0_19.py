from bz2 import BZ2Decompressor
BZ2Decompressor.buffer_size = 1024*1024
from rsa import PublicKey
from os.path import join
from datetime import date, datetime, time
from json import loads

# standard library
from collections import namedtuple
from itertools import chain
from operator import attrgetter
from xml.dom.minidom import parseString
from xml.dom.minidom import parse
from csv import DictReader

def prepare_library(logger, library_dir):
    logger.info("parsing the ALTO xml files to extract line positions")
    lib = parse_alto_dir(library_dir, logger)
    logger.info("dumping the library to disk")
    dump_library(lib, "/tmp/library.p", logger)
    return lib
        
def prepare_books(logger, library, mets_dir):
    logger.info("converting the METS files in %s" % mets_dir)
    for metsfile in list_mets(mets_dir):
        try:
            parse_mets(metsfile, logger, library)
