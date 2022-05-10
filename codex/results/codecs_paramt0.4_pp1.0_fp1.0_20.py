import codecs
codecs.register_error('strict', codecs.ignore_errors)

# -----------------------------------------------------------------------------
#
#   Main script
#
# -----------------------------------------------------------------------------

#
#   Constants
#

#   The name of the file that contains the list of files to be processed
#   (relative to the current directory)

FILENAME_LIST = './filelist.txt'


#   The name of the output file (relative to the current directory)

FILENAME_OUTPUT = './output.txt'


#   The name of the file that contains the list of words to be searched
#   (relative to the current directory)

FILENAME_WORDS = './words.txt'


#   The encoding of the input files

ENCODING = 'utf-8'


#   The encoding of the output file

OUTPUT_ENCODING = 'utf-8'


#   The encoding of the words file

WORDS_ENCODING = 'utf-8'


#   The encoding of the file list

LIST_ENCODING = 'utf-8'


#   The
