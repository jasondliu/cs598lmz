import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

# Set up command line arguments
parser = argparse.ArgumentParser(description='Removes matching lines from a CSV file.')
parser.add_argument('-i', '--input', type=str, required=True, help='Input CSV file')
parser.add_argument('-o', '--output', type=str, required=True, help='Output CSV file')
parser.add_argument('-f', '--field', type=int, required=True, help='Field')
parser.add_argument('-v', '--value', type=str, required=True, help='Value')
parser.add_argument('-c', '--case
