import codecs
# Test codecs.register_error('some-encoding', SomeReplacer)
replacer = codecs.make_replacement_error('stuff')
assert replacer == 'stuff'

# Test registering an error handler
encodingErrorHandler = codecs.make_error_handler(self)
codecs.register_error('some-encoding', encodingErrorHandler)


# Custom unicode character
# http://stackoverflow.com/questions/8158685/what-is-the-difference-between-u200bu200b-and-u200b?noredirect=1#comment12066896_8158685
