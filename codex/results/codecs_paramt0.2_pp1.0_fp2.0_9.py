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

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate a list of all the '
                                     'files in a directory and its subdirectories.')
    parser.add_argument('directory', help='the directory to start from')
    parser.add_argument('-o', '--output', help='the output file')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='print the file list to stdout')
    args = parser.parse_args()

    # Get the list of files
    file_list = get_file_list(args.directory)

    # Print the file list to stdout
    if args.verbose:
        for f in file_list:
            print(f)

    # Write the file list to a file
    if args
