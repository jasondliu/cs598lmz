import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Set up the command line arguments
parser = argparse.ArgumentParser(description='Convert a CSV file to a JSON file.')
parser.add_argument('--csv', dest='csv_file', required=True, help='The CSV file to convert.')
parser.add_argument('--json', dest='json_file', required=True, help='The JSON file to create.')
parser.add_argument('--encoding', dest='encoding', default='utf-8', help='The encoding of the CSV file.')
parser.add_argument('--delimiter', dest='delimiter', default=',', help='The delimiter of the CSV file.')
parser.add_argument('--quotechar', dest='quotechar', default='"', help='The quote character of the CSV file.')
parser.add_argument('--escapechar', dest='escapechar', default='
