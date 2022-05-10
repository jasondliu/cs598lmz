import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
import os
import csv
import glob
from unicodedata import normalize
from shutil import copyfile
from datetime import datetime
from time import time
from zipfile import ZipFile
from lxml import etree
from portality.core import app
from portality.clcsv import UnicodeDictReader, UnicodeReader
from portality.models import Account, Journal
from portality.bll import DOAJ
from portality.bll.remote_account import RemoteAccount
import xml.etree.ElementTree as ET

def main():
    start = time()

    # Check run earliest time (to stop clashes with lcc)
    run_earliest = datetime.now()
    run_earliest = run_earliest.replace(minute=run_earliest.minute+2)
    if datetime.now() < run_earliest:
        print 'Too early - aborting'
        print 'Current time: ' + str(datetime.now())
        print 'Run
