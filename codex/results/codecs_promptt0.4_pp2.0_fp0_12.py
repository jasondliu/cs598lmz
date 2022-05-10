import codecs
# Test codecs.register_error
def my_handler(exception):
    return ('', exception.end)
codecs.register_error('my_handler', my_handler)
codecs.register_error('my_handler', my_handler)

# Test codecs.lookup_error
codecs.lookup_error('my_handler')
codecs.lookup_error('my_handler')

# Test codecs.strict_errors
codecs.strict_errors
codecs.strict_errors

# Test codecs.replace_errors
codecs.replace_errors
codecs.replace_errors

# Test codecs.ignore_errors
codecs.ignore_errors
codecs.ignore_errors

# Test codecs.xmlcharrefreplace_errors
codecs.xmlcharrefreplace_errors
codecs.xmlcharrefreplace_errors

# Test codecs.backslashreplace_errors
codecs.backslashreplace_errors
codecs.backslashreplace_errors

# Test codecs.nameprep_errors
cod
