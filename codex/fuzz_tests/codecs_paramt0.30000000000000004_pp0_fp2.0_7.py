import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up the command line arguments
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-i', '--input', help='input JSON file', required=True)
parser.add_argument('-o', '--output', help='output JSON file', required=True)

args = parser.parse_args()

input_file = args.input
output_file = args.output

logger.info("Reading lines from file at: " + input_file)
logger.info("Writing lines to file at: " + output_file)

data = []
with open(input_file, 'r') as f:
    for line in f:
        data.append(json.loads(line))

logger.info("Read " + str(len(data)) + " lines")

# Create a set of unique words
unique_words = set
