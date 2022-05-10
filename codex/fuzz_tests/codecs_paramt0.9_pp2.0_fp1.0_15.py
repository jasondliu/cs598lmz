import codecs
codecs.register_error('skip', lambda error: (u'\xa0', error.start + 1))

diacritics = {}

# diacritics and hyphens are one-to-many mappings
# so we are putting them in a dictionary
diacritics['(à|À|à|À|Â|â|Â|â|ầ|ầ|Ấ|ấ|ă|Ă|ằ|ằ|Ắ|ắ|ẳ|ẳ|Ẳ|Ẳ|ẵ|ẵ|Ẵ|Ẵ|ặ|ặ|Ặ|Ặ|ạ|ạ|Ạ|Ạ)'] = u'a'
diacritics['(ã|Ã|ả|Ả|ẳ|ẳ|Ẳ|Ẳ|ẵ|ẵ|Ẵ|Ẵ|ặ|ặ|Ặ|
