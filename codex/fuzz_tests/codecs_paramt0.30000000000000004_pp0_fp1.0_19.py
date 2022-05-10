import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path \
    import join, exists

from os \
    import makedirs

from subprocess \
    import Popen, PIPE

from sys \
    import argv, exit, stdout, stderr

from time \
    import time

from optparse \
    import OptionParser

#-------------------------------------------------------------------------------
#  Constants:
#-------------------------------------------------------------------------------

# The name of the script:
ScriptName = argv[0]

# The name of the script without the extension:
ScriptNameBase = ScriptName[ : ScriptName.rfind( '.' ) ]

# The name of the log file:
LogFileName = ScriptNameBase + '.log'

# The name of the output file:
OutputFileName = ScriptNameBase + '.out'

# The name of the output file:
ErrorFileName = ScriptNameBase + '.err'

# The name of the output file:
DiffFileName = ScriptNameBase + '.diff'
