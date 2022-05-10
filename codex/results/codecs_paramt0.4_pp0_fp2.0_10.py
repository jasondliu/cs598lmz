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
#  Get command line arguments
#
if len(sys.argv) != 3:
    print('usage: %s <input file> <output file>' % sys.argv[0])
    sys.exit(1)

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

#
#  Read input file
#
input_file = codecs.open(input_file_name, 'r', 'utf-8', 'strict')
input_text = input_file.read()
input_file.close()

#
#  Parse input file
#
parser = Parser()
parser.parse(input_text)

#
#  Write output file
#
output_file = codecs.open(output_file_name, 'w', 'utf-8', 'strict')

