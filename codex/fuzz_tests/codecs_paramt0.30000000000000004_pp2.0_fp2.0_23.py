import codecs
codecs.register_error('strict', codecs.ignore_errors)

#
#  This is the main function to be called by the user.
#
def convert(source, target, options=None):
    if options is None:
        options = {}

    #
    #  Set up the options.
    #
    if 'verbose' in options:
        verbose = options['verbose']
    else:
        verbose = False

    if 'debug' in options:
        debug = options['debug']
    else:
        debug = False

    if 'encoding' in options:
        encoding = options['encoding']
    else:
        encoding = 'utf-8'

    if 'encoding_errors' in options:
        encoding_errors = options['encoding_errors']
    else:
        encoding_errors = 'strict'

    if 'encoding_output' in options:
        encoding_output = options['encoding_output']
    else:
        encoding_output = 'utf-8'

    if 'encoding_output_errors' in options:
        encoding_output
