import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Set up logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                    level=logging.INFO)

# Set up the command line arguments
parser = argparse.ArgumentParser(description='Train a word2vec model.')
parser.add_argument('-i', '--input', dest='input',
                    help='Input file containing the corpus.')
parser.add_argument('-o', '--output', dest='output',
                    help='Output file to save the model.')
parser.add_argument('-s', '--size', dest='size', type=int, default=100,
                    help='Size of the word vectors.')
parser.add_argument('-w', '--window', dest='window', type=int, default=5,
                    help='Size of the context window.')
parser.add_argument('-m', '--min-count', dest='min_count', type=int, default=5,
                    help='Minimum frequency of words.'
