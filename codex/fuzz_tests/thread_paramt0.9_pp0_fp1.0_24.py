import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()

# Write a hello message
import re
print("\n%s\n\n" % re.sub(r"\n.*\Z", "", open(__file__).read()), file=sys.stderr)

# Load the data in
import csv
reader = csv.reader(
    open('/Users/hoeflingtw/Downloads/typed-data-sets-bb9e0f08/data/norm.csv'))
data = [(row[:5],row[5:6]) for row in reader]
train,test = data[1:],data[:1]

# Data transformation and munging
import math, random
from collections import Counter
from itertools import izip_longest as zip_longest
from random import choice, shuffle, normalvariate
##
# Compare two scores based on precision and recall measures
def comparison(left,right):
  def safe_division(a,b): return 0 if b==0 else a/float(b)
  pc = safe_division(left
