import mmap
import math
import sys
import os
#import operator
from operator import itemgetter, attrgetter


def main():

    ####  check argument which is input file #####    
    if len(sys.argv) < 3 :
        print "usage : python %s input_file output_file" % (sys.argv[0])
        sys.exit(-1)
        
    result = {}
    cnt = 0
    f = open("%s" % (sys.argv[1]))
    lines = f.readlines()
    for line in lines :
        line = line.strip()
        cols = line.split("\t")
        #print cols
        y = cols[1]
        if result.has_key(y) == False :
            result[y] = 1
        else :
            result[y] = result[y] + 1
        cnt = cnt + 1

    for y in sorted(result.keys()) :
        print y + "\t" + str(result[y]) + "\t" + str(float
