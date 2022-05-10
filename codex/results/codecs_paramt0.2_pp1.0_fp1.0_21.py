import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Set up logging
logger = logging.getLogger(__name__)

# Set up the command-line options
desc = """
Accepts a file containing a list of IDs and a directory containing
files with those IDs and outputs a new directory containing only
those files.
"""

parser = argparse.ArgumentParser(description=desc)

parser.add_argument("--debug",
                    action='store_true',
                    help="Print debug messages to standard out.")
parser.add_argument("--input",
                    help="The file containing the list of IDs.")
parser.add_argument("--input-dir",
                    help="The directory containing the files to be filtered.")
parser.add_argument("--output-dir",
                    help="The directory to write the filtered files to.")

def main():
    """
    Parses command line arguments and does the work of the program.
    """
    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger
