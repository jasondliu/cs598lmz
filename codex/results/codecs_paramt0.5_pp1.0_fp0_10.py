import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def main(args):
    # check parameters
    if len(args) < 3:
        sys.stderr.write("Usage: %s INPUT_FILE OUTPUT_FILE\n" % args[0])
        return 1
    if not os.path.isfile(args[1]):
        sys.stderr.write('"%s" is not a file.\n' % args[1])
        return 1

    # read input file
    sys.stderr.write('Loading "%s"...\n' % args[1])
    try:
        with codecs.open(args[1], 'r', 'utf-8', 'replace_with_space') as input_file:
            lines = [line.rstrip('\r\n') for line in input_file]
    except IOError as e:
        sys.stderr.write("Failed to read file: %s\n" % e)
        return 1

    # convert
    sys.stderr.write('Con
