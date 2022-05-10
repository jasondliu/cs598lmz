import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# Global variables
verbose = False

#
#  MAIN
#
if __name__ == '__main__':
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], 'v', ['verbose'])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, val in opts:
        if opt in ['-v', '--verbose']:
            verbose = True

    if len(args) < 2:
        usage()
        sys.exit(2)

    # Process arguments
    input_file = args[0]
    output_file = args[1]

    # Check if input file exists
    if not os.path.isfile(input_file):
        print("Input file '{0}' does not exist".format(input_file))
        exit(1)

    # Convert file
    process(input_file,
