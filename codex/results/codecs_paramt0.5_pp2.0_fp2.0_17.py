import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main(args):
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Convert a text file to a '
                                                 'list of tuples.')
    parser.add_argument('input_file',
                        help='input file')
    parser.add_argument('output_file',
                        help='output file')
    parser.add_argument('-s', '--separator', default='\t',
                        help='separator character')
    parser.add_argument('-l', '--line-separator', default='\n',
                        help='line separator character')
    parser.add_argument('-c', '--columns', type=int, default=2,
                        help='number of columns')
    parser.add_argument('-e', '--encoding', default='utf-8',
                        help='encoding')
    args = parser.parse_args(args)

    # Read input file
    with codecs.open(args.input_file, 'r', args.
