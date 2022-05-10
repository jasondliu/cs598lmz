import codecs
codecs.register_error("strict", codecs.ignore_errors)

import matplotlib.pyplot as plt
import numpy as np

N_HISTS = 5

def main(args):
    if args.infile is None:
        raise ValueError("infile not given")
    infile = args.infile
    outfile = args.outfile
    '''
    if len(args.infile) == 1:
        infile = args.infile[0]
    elif len(args.infile) >= 2:
        file_freq = {file:0 for file in args.infile}
        for file in args.infile:
            count = 0
            with codecs.open(file, 'r', 'utf-8') as fp:
                for _ in fp:
                    count += 1
            file_freq[file] = count
        sorted_freq = sorted(file_freq.items(), key=lambda x:x[1], reverse=True)
        infile = [x for x, _ in sorted_freq]
    '
