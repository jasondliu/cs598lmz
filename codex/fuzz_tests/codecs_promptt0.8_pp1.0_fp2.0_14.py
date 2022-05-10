import codecs
# Test codecs.register_error('ignore', codecs.ignore_errors)
codecs.register_error('ignore', codecs.ignore_errors)

def _get_encoding(mbcs):
    # Return the character encoding used in a MBCS encoded string.
    #
    # "mbcs" is a string, encoded in MBCS, that we wish to check.
    #
    # Returns the character encoding used (e.g. 'mbcs' or 'oem').
    # Note that 'mbcs' can be used to encode both MBCS and UTF-16
    # strings.  In the case of UTF-16, we return 'utf16' (which
    # is not a valid encoding name).  For 'oem' we return 'oem+<codepage>'.

    #
    # This uses ctypes, and currently only works on Windows.
    #
    if not isinstance(mbcs, str):
        raise TypeError('mbcs argument must be a string')
    # Get the code-page used to encode the string.
    if sys.platform == 'win32':
        import c
