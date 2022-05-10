import codecs
codecs.register_error('replace_with_space', codecs.replace_errors(u' \ufffd ')) # python2
#codecs.register_error('replace_with_space', codecs.replace_errors('\ufffd'))  # python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--raw_data', type=str, default='raw_data')
parser.add_argument('--test', action='store_true')
parser.add_argument('--save_data', type=str, default='data')
parser.add_argument('--lower', action='store_true')
parser.add_argument('--ngram_size', type=int, default=3)
parser.add_argument('--ngram_noverlap', action='store_true')
parser.add_argument('--min_freq', type=int, default=5)
parser.add_argument('--shuffle', action='store_true')
parser.add_argument('--seed', type=int, default=123)
parser.add_argument('--split_ratio',
