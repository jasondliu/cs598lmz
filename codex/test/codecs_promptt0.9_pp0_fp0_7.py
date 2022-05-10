import codecs
# Test codecs.register_error

# u"\ubc16" escapes weren't supported by "unicode-internal"
def unrepr(self, input):
    if input[:2] == 'u"':
        return (input[1:], 2)
codecs.register_error('test.readerror', unrepr)

