import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _get_encoding(f):
    """
    Return the encoding of the file f.
    """
    # XXX: this is a hack to work around the fact that
    #      the codecs module doesn't have a way to
    #      detect the encoding of a file
    #      (see http://bugs.python.org/issue10304)
    #      The code is taken from the codecs module.
    #      It's a bit fragile, but it works.
    #      If this doesn't work for you, please
    #      file a bug report.
    #
    #      Note that this function is only used
    #      when the user doesn't specify an encoding.
    #      If the user specifies an encoding,
    #      we use the codecs module to open the file.
    #      In that case, the codecs module will
    #      detect the encoding for us.
    #
    #      Note that this function is only used
    #      when the user doesn't specify an encoding.
    #      If the user specifies
