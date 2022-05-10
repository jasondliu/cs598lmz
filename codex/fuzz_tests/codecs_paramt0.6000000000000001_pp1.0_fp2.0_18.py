import codecs
codecs.register_error('strict', codecs.lookup_error('ignore'))

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--input', type=str, default='',
                        help='path to input file')
    parser.add_argument('--output', type=str, default='',
                        help='path to output file')
    parser.add_argument('--n_threads', type=int, default=2,
                        help='number of threads to use')
    parser.add_argument('--min_len', type=int, default=1,
                        help='minimum length of sentences')
    parser.add_argument('--max_len', type=int, default=10,
                        help='maximum length of sentences')
    args = parser.parse_args()
    return args

def read_file(path):
    data = []
    with codecs.open(path, 'r', 'utf-8', 'strict') as f:
        for l in f:
            data.append(l.strip())
