import codecs
codecs.register_error('strict', codecs.ignore_errors)

#
# Globals
#

_options = None
_command = None
_args = None
_logger = None
_logger_initialized = False

#
# Functions
#

def _initialize_logger():
    global _logger_initialized

    if _logger_initialized:
        return

    _logger_initialized = True

    if _options.debug:
        level = logging.DEBUG
    elif _options.verbose:
        level = logging.INFO
    else:
        level = logging.WARNING

    logging.basicConfig(level=level, format='%(levelname)s: %(message)s')

    _logger = logging.getLogger('seafile-admin')
    _logger.setLevel(level)

def _parse_options():
    global _options
    global _command
    global _args

    parser = OptionParser()

    parser.add_option('-c', '--config-file', dest='config_file',
                      default='/etc/se
