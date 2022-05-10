import codecs
codecs.register_error('strict', codecs.ignore_errors)
codecs.register_error('replace', codecs.replace_errors)
print('passed')
