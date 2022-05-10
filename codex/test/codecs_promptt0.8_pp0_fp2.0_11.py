import codecs
# Test codecs.register_error for embedded 'strict' error handler

handler_map = codecs.make_identity_dict(range(256))
