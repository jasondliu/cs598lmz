from bz2 import BZ2Decompressor
BZ2Decompressor.decompress =  lambda x: bz2.decompress(x)
BZ2Decompressor.flush = lambda x : x
del BZ2Decompressor


import theano.tensor as T
from theano import function,config, shared
import numpy
import time
from operator import attrgetter

from theano.sandbox.rng_mrg import MRG_RandomStreams as RandomStreams



# get the list of files
os.chdir(options.inputdir)
import glob
files = glob.glob("*.part*")
files.sort()


# create the output file
output = open(options.outputfile,"w")


# create a generator for the files
def file_generation(files):
    for f in files:
        for line in open(f):
            yield line

# create a generator for the batches
def batch_generator(lines):
    for line in lines:
        if line[0]=='#':
            continue
        cols=line[:-1].split(' ')
        source = T.
