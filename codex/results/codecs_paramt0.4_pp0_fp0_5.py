import codecs
codecs.register_error('strict', codecs.ignore_errors)

def parse_args():
    parser = argparse.ArgumentParser(description='Create a word2vec model from a corpus.')
    parser.add_argument('-c', '--corpus', help='Corpus file', required=True)
    parser.add_argument('-m', '--model', help='Output model file', required=True)
    parser.add_argument('-v', '--vocab', help='Output vocabulary file', required=True)
    parser.add_argument('-n', '--ngram', help='Ngram size', type=int, default=1)
    parser.add_argument('-s', '--size', help='Embedding size', type=int, default=100)
    parser.add_argument('-w', '--window', help='Window size', type=int, default=5)
    parser.add_argument('-t', '--threads', help='Number of threads', type=int, default=1)
    parser.add_argument('-i', '--iterations', help='
