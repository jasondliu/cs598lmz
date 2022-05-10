import codecs
codecs.register_error('strict', codecs.ignore_errors)

def parse_args():
    parser = argparse.ArgumentParser(description='Compute the BLEU score for a corpus')
    parser.add_argument('-r', '--reference', nargs='+', help='Path to reference corpus')
    parser.add_argument('-c', '--candidate', nargs='+', help='Path to candidate corpus')
    parser.add_argument('-b', '--bpe', help='Apply BPE to the corpus')
    parser.add_argument('-n', '--n', help='Compute BLEU-n score', type=int, default=4)
    parser.add_argument('-l', '--lowercase', help='Lowercase the corpus', action='store_true')
    parser.add_argument('-s', '--smooth', help='Smooth the BLEU score', action='store_true')
    parser.add_argument('-t', '--tokenize', help='Tokenize the corpus', action='store_true')
    parser.add_argument('-v
