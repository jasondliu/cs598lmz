import codecs
# Test codecs.register_error(decoder)
# Make sure that the implicit utf-8 codec can be used with
# error handler.

codecs.register_error("custom", codecs.ignore_errors)
