import codecs
# Test codecs.register_error.
codecs.register_error('bad_error', lambda obj: (u'', obj.start + 1))

