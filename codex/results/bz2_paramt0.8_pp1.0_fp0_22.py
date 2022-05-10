from bz2 import BZ2Decompressor
BZ2Decompressor(open('030401.zip.bz2'))

regex = r'A(B|C)'

for line in  sys.stdin:
    line = line.rstrip()
    # process line

import re, sys

regex = r'A(B|C)'

for line in sys.stdin:
    line = line.rstrip()
    if re.search(regex, line):
        print line

import re

regexs = ['A(B|C)', 'D(E|F)']

re.compile(regexs[0])
regexs = [re.compile(regex) for regex in regexs]
res = [regex.search(line) for regex in regexs]


import re

regexs = ['A(B|C)', 'D(E|F)']
line = sys.stdin.readline().rstrip()

line = line.rstrip()
_ = [print(line) for regex in regexs if re.search(regex, line)]


