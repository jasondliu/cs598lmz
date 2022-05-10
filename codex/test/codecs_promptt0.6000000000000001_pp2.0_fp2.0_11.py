import codecs
# Test codecs.register_error
try:
    codecs.register_error('spam', 'eggs')
except TypeError:
    pass
else:
    print('Failed to raise TypeError for spam error handler')

