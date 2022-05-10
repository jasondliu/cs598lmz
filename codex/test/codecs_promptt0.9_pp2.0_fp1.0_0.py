import codecs
# Test codecs.register_error()
codecs.register_error('strict', codecs.strict_errors)
codecs.register_error('ignore', codecs.ignore_errors)
codecs.register_error('replace', codecs.replace_errors)
# Please don't escape the encoding here
encoding = '\u00e0'

def check(errors):
    result = codecs.lookup_error(errors)
    if len(result) != 2:
        raise Exception("lookup_error didn't return a tuple of length 2")
    (handler, new_errors) = result
    if errors is new_errors:
        raise Exception("lookup_error didn't copy errors")
    return handler, new_errors

# Test with encode()
