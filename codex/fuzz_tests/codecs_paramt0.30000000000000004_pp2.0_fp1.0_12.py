import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    # Get the input file name
    if len(sys.argv) < 2:
        print "Usage: python %s <input_file>" % sys.argv[0]
        sys.exit(0)
    input_file = sys.argv[1]

    # Open the input file
    try:
        input_fd = codecs.open(input_file, 'r', 'utf-8', 'strict')
    except IOError:
        print "Error: cannot open file %s" % input_file
        sys.exit(1)

    # Read the input file
    input_data = input_fd.read()
    input_fd.close()

    # Create the output file
    output_file = input_file + ".out"
    try:
        output_fd = codecs.open(output_file, 'w', 'utf-8', 'strict')
    except IOError:
        print "Error: cannot open file %s" % output_file
        sys.exit(1)
