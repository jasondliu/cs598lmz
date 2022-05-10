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

