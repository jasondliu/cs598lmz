import codecs
# Test codecs.register_error()
def my_error(err):
    print(err)
codecs.register_error('CustomError', lambda err: (u'ERROR', err.end))
for encoding in ['rot13', 'utf-16']:
    codecs.register_error('CustomError', my_error)
    try:
        print(u'{} encoded string:'.format(encoding))
        print(u'\t{}'.format(bytes(encoded_texts[encoding], encoding=encoding), encoding=encoding))
    except UnicodeEncodeError as err:
        print(u'ERROR (UncodeEncodeError raised)')
        print(u'\t{}'.format(str(err)))
    except UnicodeDecodeError as err:
        print(u'ERROR (UnicodeDecodeError raised)')
        print(u'\t{}'.format(str(err)))

# Test codecs.lookup()
print(u"\nCodecs lookup for 'utf-8':")
print(u'\t{}'.format(codecs.
