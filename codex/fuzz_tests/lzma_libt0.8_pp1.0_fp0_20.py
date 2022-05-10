import lzma
lzma.__name__

import sys
print(sys.version)

import shlex

import os

import glob

def natural_sort(l): 
  import re
  convert = lambda text: int(text) if text.isdigit() else text.lower() 
  alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
  return sorted(l, key = alphanum_key)

## open SVM file
print("\nCompute SVM scores")

f = open(args.DATA_PATH,"r")

## open results file
f2 = open(args.RESULTS_PATH,"w")

DATASET=""
trial=""
trajectory=""

RESULTS_DICTIONARY={}

# read files, one file at a time
for line in f:

  #if line[0]=="#":
  #  continue

  line = line.strip()
  lines = shlex.split(line)

  if len(lines)<4
