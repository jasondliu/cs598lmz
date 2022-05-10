import codecs
# Test codecs.register_error

# This test is here because the codecs module has a private
# _codecs_cn module, which is imported by the _multibytecodec
# module.  It is needed to test the ascii codec.

