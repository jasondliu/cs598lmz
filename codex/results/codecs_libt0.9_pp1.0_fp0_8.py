import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)
##sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='cp65001')

################################################################################

from visa import Instrument, VisaIOError
from time import sleep
import visa

################################################################################

import argparse
################################################################################

from DriftTester import DriftTester
from GUIApplicationDT import GUIApplicationDT
from cliApplicationDT import cliApplicationDT

################################################################################

def get_args():
    parser = argparse.ArgumentParser(description='DriftTester class')
    parser.add_argument('-g','--gui',required=False, action="store_true", help='GUI')
    parser.add_argument('-d','--debug',required=False, action="store_true", help='Debug')
    parser.add_argument('-t','--test',required=False, action="store_true", help='Test')
    parser.add_argument('--vna',required=
