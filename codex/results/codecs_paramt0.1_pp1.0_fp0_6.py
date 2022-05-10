import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, dirname, abspath, exists

from os \
    import makedirs

from sys \
    import argv

from glob \
    import glob

from re \
    import compile

from shutil \
    import copyfile

from subprocess \
    import Popen, PIPE

#-------------------------------------------------------------------------------
#  Constants:
#-------------------------------------------------------------------------------

# The name of the file containing the list of files to be copied:
FileList = 'file_list.txt'

# The name of the file containing the list of files to be copied:
FileList2 = 'file_list2.txt'

# The name of the file containing the list of files to be copied:
FileList3 = 'file_list3.txt'

# The name of the file containing the list of files to be copied:
FileList4 = 'file_list4.txt'

# The name of the file containing the list of files
