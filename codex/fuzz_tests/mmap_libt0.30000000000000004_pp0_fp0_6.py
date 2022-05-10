import mmap
import re
import sys

from . import __version__


def main():
    """
    Main function.
    """
    # Parse command line arguments.
    args = parse_args()

    # Print version information if requested.
    if args.version:
        print('{} {}'.format(os.path.basename(sys.argv[0]), __version__))
        sys.exit(0)

    # Print help information if requested.
    if args.help:
        print(__doc__)
        sys.exit(0)

    # Check that the input file exists.
    if not os.path.isfile(args.input):
        print('Input file not found: {}'.format(args.input))
        sys.exit(1)

    # Check that the input file is not empty.
    if os.path.getsize(args.input) == 0:
        print('Input file is empty: {}'.format(args.input))
        sys.exit(1)

    # Check that the output file does not exist.
    if os.path.isf
