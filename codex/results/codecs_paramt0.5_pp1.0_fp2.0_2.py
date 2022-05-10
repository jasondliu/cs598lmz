import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# Set the default encoding to utf-8
# This is now done in site.py so it should not be needed.
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

# The base implementation of create_parser is not unicode-safe
# because it does not use codecs.open for reading files.

import optparse

# Patch optparse to use codecs.open
#
def create_parser():
    """Return an OptionParser for command line options."""
    from calibre import prints
    from calibre.utils.logging import Log
    parser = optparse.OptionParser(usage=_('\n\n%prog [options] file'))
    parser.add_option('-f', '--file', dest='file', default=None,
            help=_('The input file to use. The input file must be a '
                'valid EPUB file. If this option is not specified, the '
                'input file is read from STDIN.'))
