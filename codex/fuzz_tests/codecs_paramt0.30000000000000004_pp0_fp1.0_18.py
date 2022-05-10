import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up the command line arguments
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-i', '--input', help="Input file to be read. Reads from stdin if not set.")
parser.add_argument('-o', '--output', help="Output file to be written to. Writes to stdout if not set.")
parser.add_argument('-v', '--verbose', action='store_true', help="Increase output verbosity")
args = parser.parse_args()

if args.verbose:
    logger.setLevel(logging.DEBUG)

logger.debug("Input: %s Output: %s Verbose: %s", args.input, args.output, args.verbose)

# Set up input and output
if args.input:
    input_file = codecs.open(args.input, 'r
