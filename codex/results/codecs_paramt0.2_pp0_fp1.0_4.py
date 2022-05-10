import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Set up logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)

# Set up the command line arguments
parser = argparse.ArgumentParser(description='Train a word2vec model.')
parser.add_argument('-train', help='Training file', required=True)
parser.add_argument('-output', help='Output model file', required=True)
parser.add_argument('-size', type=int, help='Embedding size', default=100)
parser.add_argument('-window', type=int, help='Max distance between the current and predicted word', default=5)
parser.add_argument('-sample', type=float, help='Threshold for occurrence of words', default=1e-3)
parser.add_argument('-negative', type=int, help='Number of negative examples', default=5)
parser.add_argument('-threads', type=int, help='Number of threads', default=12)

