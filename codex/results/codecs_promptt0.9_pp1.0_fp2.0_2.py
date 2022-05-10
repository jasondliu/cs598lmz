import codecs
# Test codecs.register_error('test', my_error_handler)

#------------------------------------------------------------------------------
# Windows Users
#------------------------------------------------------------------------------
# If you want to use this program on Windows and encounter an error (UnicodeEncodeError),
# uncomment the following two lines and replace USERNAME with your account's name:
#import locale
#locale.setlocale(locale.LC_ALL, "USERNAME")

#------------------------------------------------------------------------------
# A Simple Music Library Renamer
#------------------------------------------------------------------------------
# This simple script will look for .mp3 files in the current directory that are
# incorrectly named and rename them according to the following rules:
# - Remove all non-letter/numbers/spaces characters from the filename.
# - Remove any file extension.
# - Split the filename by the number of parts provided.
# - Capitalize the first letter of each name part.
#
# It will then append the original extention back to the name. It will not
# overwrite any files if a file already exists with the new name.
# The output will be redirected to the console. You can pipe it into a file.
# The default mode is './test_files/
