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

#
#  Retrieve program name.
#
program = os.path.basename(sys.argv[0])

#
#  Verify and process command line options.
#
if (len(sys.argv) != 2):
    print('Usage: %s <input file>' % program)
    sys.exit(1)

#
#  Open input file.
#
try:
    input_file = codecs.open(sys.argv[1], 'r', 'utf-8', 'strict')
except IOError as e:
    print('%s: Cannot open input file: %s' % (program, e.strerror))
    sys.exit(1)

#
#  Read input file.
#
try:
    input_text = input_file.read()
except IOError as e:
    print('%s: Cannot read
