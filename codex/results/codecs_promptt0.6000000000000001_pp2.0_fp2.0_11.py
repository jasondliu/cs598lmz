import codecs
# Test codecs.register_error
try:
    codecs.register_error('spam', 'eggs')
except TypeError:
    pass
else:
    print('Failed to raise TypeError for spam error handler')

try:
    codecs.register_error('stderror', codecs.stderror_encode)
except TypeError:
    pass
else:
    print('Failed to raise TypeError for stderror error handler')

class Spam:
    def __init__(self, errors):
        self.errors = errors
    def __call__(self, exception):
        return ('spam', 'eggs', exception.start + 3)

try:
    codecs.register_error('spamhandler', Spam)
except TypeError:
    pass
else:
    print('Failed to raise TypeError for spam error handler')

class Spam:
    def __init__(self, errors):
        self.errors = errors
    def __call__(self, exception):
        return ('spam', 'eggs', exception.start + 3)

class Eggs:
