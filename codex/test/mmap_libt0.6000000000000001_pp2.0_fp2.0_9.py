import mmap
import os, sys
import re
import subprocess
import shutil
import gzip
import argparse
import warnings
from datetime import datetime

warnings.filterwarnings("ignore", category=DeprecationWarning)

parser = argparse.ArgumentParser(description='Parse and create a new data.tsv file with a new column with the # of reads in each sample')
parser.add_argument('-i', '--input', help='Input data.tsv file', required=True)
parser.add_argument('-r', '--reads_dir', help='Path to the reads directory', required=True)
parser.add_argument('-o', '--output', help='Output data.tsv file', required=True)
