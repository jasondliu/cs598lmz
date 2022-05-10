import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Set up logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

# Set up command line argument parsing
parser = argparse.ArgumentParser(description='Generate a list of all the '
                                 'words in a text file.')
parser.add_argument('input_file', type=str,
                    help='The file to read from.')
parser.add_argument('output_file', type=str,
                    help='The file to write to.')
parser.add_argument('--encoding', type=str, default='utf-8',
                    help='The encoding of the input file.')
parser.add_argument('--lowercase', action='store_true',
                    help='Convert all words to lowercase.')
parser.add_argument('--min
