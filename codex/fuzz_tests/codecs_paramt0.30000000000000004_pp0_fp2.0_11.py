import codecs
codecs.register_error('strict', codecs.ignore_errors)

#------------------------------------------------------------------------------
#
#  Functions
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#
#  Main program
#
#------------------------------------------------------------------------------

if __name__ == '__main__':
    #
    #  Cmd line args
    #
    parser = argparse.ArgumentParser(description='Convert a CSV file to a JSON file')
    parser.add_argument('--csv', help='CSV filename', required=True)
    parser.add_argument('--json', help='JSON filename', required=True)
    parser.add_argument('--encoding', help='CSV file encoding', default='utf-8')
    parser.add_argument('--delimiter', help='CSV file delimiter', default=',')
    parser.add_argument('--quotechar', help='CSV file quote character', default='"')
    args = parser.parse_args()

    #
    #  Read CSV file
    #
    with codecs.open(args.csv, 'r', args.encoding, 'strict
