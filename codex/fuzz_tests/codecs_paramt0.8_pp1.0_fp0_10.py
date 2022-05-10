import codecs
codecs.register_error("replace_with_space", codecs.replace_with(" "))

# Ensure we have support for unicode file names
_sys_encoding = sys.getfilesystemencoding()

def _argv_to_unicode():
    # On Mac OS X, getfilesystemenoding() is 'utf-8' but mbcs is used.
    if sys.platform == 'darwin' and _sys_encoding == 'utf-8':
        encoding = 'mbcs'
    else:
        encoding = _sys_encoding
    return [ arg.decode(encoding, 'replace_with_space')
             for arg in sys.argv ]

def main(argv=None):
    """Main program.

    @param argv: Command line arguments
    @type argv: list of unicode
    
    @return: exit code
    @rtype: int
    """
    if argv is None:
        argv = _argv_to_unicode()
    path = os.path.dirname(os.path.abspath(argv[0
