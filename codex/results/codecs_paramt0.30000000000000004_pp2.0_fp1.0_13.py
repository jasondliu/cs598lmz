import codecs
codecs.register_error('strict', codecs.ignore_errors)

# from http://stackoverflow.com/questions/19278845/how-to-use-python-to-convert-utf-8-encoded-strings-to-ascii
# and http://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def remove_accents_and_lower(input_str):
    return remove_accents(input_str).lower()

def remove_accents_and_lower_and_punct(input_str):
    return remove_accents(input_str).lower().translate(None, string.punctuation)

def remove_accents_and_lower_
