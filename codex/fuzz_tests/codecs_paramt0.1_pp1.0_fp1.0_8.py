import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up the command line arguments
parser = argparse.ArgumentParser(description='Convert a CSV file to a JSON file.')
parser.add_argument('csv_file', help='The CSV file to convert.')
parser.add_argument('json_file', help='The JSON file to write to.')
parser.add_argument('--encoding', help='The encoding of the CSV file.', default='utf-8')
parser.add_argument('--delimiter', help='The delimiter of the CSV file.', default=',')
parser.add_argument('--quotechar', help='The quote character of the CSV file.', default='"')
parser.add_argument('--escapechar', help='The escape character of the CSV file.', default='\\')
parser.add_argument('--skip-header', help='Skip the first line of the CSV file.', action='store_true')
parser
