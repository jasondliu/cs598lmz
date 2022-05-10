import mmap
import sys
import re
import os
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    stream=sys.stdout)

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--infile", help="File to analyze", type=str, required=True)
parser.add_argument("-o", "--outfile", help="Output file", type=str, required=True)
parser.add_argument("-m", "--max_lines", help="Max lines to analyze", type=int, default=10000)
parser.add_argument("-p", "--pattern", help="Regex pattern to match", type=str, default=r"^\[\d+\]")
parser.add_argument("-s", "--step", help="Step between each line", type=int, default=1)
parser.add_argument("-t", "--threshold", help="Threshold for number of matches", type=int, default
