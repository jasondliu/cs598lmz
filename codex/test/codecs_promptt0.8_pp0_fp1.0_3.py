import codecs
# Test codecs.register_error('ignore')
# Here, we set up ignore-encoding-errors to be
# the default.
codecs.register_error('ignore', codecs.ignore_errors)
# OK, let's try and decode this erroneous input.
