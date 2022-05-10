import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Set up the logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Set up the command line arguments
parser = argparse.ArgumentParser(description='Convert a CSV file to a JSON file')
parser.add_argument('--input', help='The CSV file to convert', required=True)
parser.add_argument('--output', help='The JSON file to create', required=True)
parser.add_argument('--encoding', help='The encoding of the CSV file', default='utf-8')
parser.add_argument('--delimiter', help='The delimiter of the CSV file', default=',')
parser.add_argument('--quotechar', help='The quote character of the CSV file', default='"')
args = parser.parse_args()

# Read the CSV file
logging.info('Reading CSV file: ' + args.input)
csv
