import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Set up logging
logger = logging.getLogger(__name__)

# Set up arguments
parser = argparse.ArgumentParser(description='Generate a context-free grammar from a training corpus.')
parser.add_argument('corpus', type=argparse.FileType('r'), help='training corpus')
parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=sys.stdout, help='output file')
parser.add_argument('-p', '--probability', type=argparse.FileType('w'), default=None, help='output file for probabilities')
parser.add_argument('-s', '--smoothing', type=float, default=0.0, help='probability smoothing')
parser.add_argument('-t', '--threshold', type=float, default=0.0, help='probability threshold')
parser.add_argument('-d', '--delimiters', type=str, default=' \t\n', help
