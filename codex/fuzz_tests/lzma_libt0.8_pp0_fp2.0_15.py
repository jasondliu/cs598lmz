import lzma
lzma.decompress()
#!/usr/bin/env python3

import os
import re
import sys
import gzip
import uproot
import glob
import json
import shutil
import numpy as np
import pandas as pd
import ROOT
from ROOT import gROOT, TFile, TTree, TChain, gDirectory, TLine, gStyle, TCanvas, TLegend, TH1F

from optparse import OptionParser
from tools import *

parser = OptionParser()

# job configuration
parser.add_option("--inputFiles", dest="inputFiles", default="data/isr_sample_small.root", help="file or list of files to process")
parser.add_option("--outputFile", dest="outputFile", default="data/isr_sample_small_processed.root", help="output file")
parser.add_option("--sampleID", dest="sampleID", default=0, help="data samples ID")
parser.add_option("--tree", dest="tree", default="tree", help="tree name")
parser.add_option("
