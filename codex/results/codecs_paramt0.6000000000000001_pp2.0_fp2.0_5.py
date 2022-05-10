import codecs
codecs.register_error('strict', codecs.ignore_errors)

# For debugging
__DEBUG__ = False

def _debug(msg):
    global __DEBUG__
    if __DEBUG__:
        print(msg)

def __init__():
    global __DEBUG__

    # Handle arguments
    parser = argparse.ArgumentParser(description='Convert a .warc file to a .json file')
    parser.add_argument('-o', '--output', metavar='output', nargs=1, type=str, help='output file', required=True)
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose output')
    parser.add_argument('-d', '--debug', action='store_true', help='debug mode')
    parser.add_argument('input', metavar='input', type=str, help='input file', nargs=1)
    args = parser.parse_args()

    # Set debug
    if args.debug:
        __DEBUG__ = True

    # Output file
    output = args.
