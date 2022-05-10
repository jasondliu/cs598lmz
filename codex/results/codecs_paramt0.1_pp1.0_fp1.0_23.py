import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

def main():
    """
    Main function.
    """

    # parse command line
    parser = argparse.ArgumentParser(description="""
    This script converts a file in the format of the Penn Treebank to the
    format of the Stanford Parser.
    """)
    parser.add_argument('--input', '-i',
                        help='input file (default: stdin)',
                        type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument('--output', '-o',
                        help='output file (default: stdout)',
                        type=argparse.FileType('w'),
                        default=sys.stdout)
    parser.add_argument('--encoding', '-e',
                        help='input file encoding (default: utf-8)',
                        default='utf-8')
    parser.add_argument('--verbose', '-v',
                        help='verbose mode (default: no)',
                        action='store_true
