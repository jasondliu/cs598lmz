import codecs
codecs.register(lambda x: lookup('utf_8') if x == 'utf8' else None)

parser = argparse.ArgumentParser(description='Applies smoothing \
                                 to a text file and outputs smoothed file.',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('input_file', type=str,
                    help='File to be smoothed')
parser.add_argument('-k', type=int, required=True,
                    help='Smoothing parameter')
parser.add_argument('-o', type=str, required=True,
                    help='Output file')
args = parser.parse_args()

with codecs.open(args.input_file, 'r', encoding='utf_8') as f:
    for line in f:
        for w in line.split():
            sorted_word = sorted(w)
            for j in range(args.k):
                sorted_word[j] = '*' 
            smoothed_word = "".join(sorted_word)
            with codec
