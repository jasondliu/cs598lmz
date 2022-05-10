import codecs
# Test codecs.register_error()
#
# We test the register_error() function, especially the "backslashreplace"
# error handler.
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).

import codecs
import StringIO

def check_error(errorhandler, input, expected):

    out = StringIO.StringIO()
    codecs.register_error(errorhandler, out.write)
    codecs.register_error('strict', None)

    # Test error handler's own write() method
    codecs.register_error(errorhandler, errorhandler.write)

    # Test error handler's own reset() method
    codecs.register_error(errorhandler, errorhandler.reset)

    # Test error handler's own handle_exception() method
    codecs.register_error(errorhandler, errorhandler.handle_exception)

    # Test error handler's own handle_error() method
    codecs.register_error(errorhandler, errorhandler.handle_error)

    # Test error handler's own handle_charref() method
    codecs.register_error(
