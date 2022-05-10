import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

# Set up command line arguments
parser = argparse.ArgumentParser(description='Generate a CSV file of the '
                                 'results of the given query.')
parser.add_argument('--query', required=True,
                    help='Path to the query file.')
parser.add_argument('--output', required=True,
                    help='Path to the output file.')
parser.add_argument('--api-key', default=os.environ.get('GOOGLE_API_KEY'),
                    help='Google API key.')
parser.add_argument('--api-secret',
                    default=os.environ.get('GOOGLE_API_SECRET'),
                    help='Google API secret.')
parser.add_argument('--api-url', default='https://www.googleapis.com/bigquery/v2',
                   
