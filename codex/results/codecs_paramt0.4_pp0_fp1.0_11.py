import codecs
codecs.register_error('strict', codecs.ignore_errors)
codecs.register_error('ignore', codecs.ignore_errors)

#
#  This is the main routine for the program.
#  It will get the command line arguments,
#  read the input file,
#  parse the input file,
#  write the output file,
#  and exit.
#
def main():
    #
    #  Get the command line arguments.
    #
    (options, args) = get_command_line_arguments()
    #
    #  Read the input file.
    #
    input_file = read_input_file(options.input_file_name)
    #
    #  Parse the input file.
    #
    parsed_input_file = parse_input_file(input_file)
    #
    #  Write the output file.
    #
    write_output_file(options.output_file_name, parsed_input_file)
    #
    #  Exit.
    #
    sys.exit(0)

#
# 
