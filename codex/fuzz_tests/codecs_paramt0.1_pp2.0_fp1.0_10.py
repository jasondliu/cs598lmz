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
#  Verify and extract arguments.
#
if (len(sys.argv) != 2):
    print(__doc__)
    sys.exit(1)

#
#  Verify that the input file exists.
#
if (not os.path.exists(sys.argv[1])):
    print("%s: Error: File '%s' does not exist." % (program, sys.argv[1]))
    sys.exit(1)

#
#  Open the input file.
#
try:
    input_file = codecs.open(sys.argv[1], 'r', 'utf-8', 'strict')
except IOError as e:
    print("%s: Error: Can't open file
