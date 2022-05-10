import codecs
# Test codecs.register_error()
codecs.register_error('error', codecs.replace_errors)
try:
    text = '\xff'.decode('ascii', 'error')
except UnicodeDecodeError:
    raise SystemError
assert text == '\ufffd'
