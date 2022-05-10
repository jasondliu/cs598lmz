import mmap
import math
import sys
import datetime
import os
import re

def main(argv):
    #print 'Number of arguments:', len(sys.argv), 'arguments.'
    #print 'Argument List:', str(sys.argv)
    #print 'Argument List:', str(sys.argv)

    # read in the arguments
    try:
        opts, args = getopt.getopt(argv,"h:",["help","infile=","outfile=","outdir="])
    except getopt.GetoptError:
        print 'parse_logs.py --infile <inputfile> --outfile <outputfile> --outdir <outputdir>'
        sys.exit(2)

    # set up the defaults
    infile = ''
    outfile = ''
    outdir = ''

    # read in the arguments
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print 'parse_logs.py --infile <inputfile> --outfile <outputfile> --
