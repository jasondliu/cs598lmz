import codecs
codecs.register_error('strict', codecs.ignore_errors)

# This is a list of all the known suffixes for the languages supported
# by the spellchecker.  The list is used to determine which dictionary
# to use for a given language.
lang_suffixes = {
    'en': '',
    'es': 'es',
    'fr': 'fr',
    'de': 'de',
    'it': 'it',
    'nl': 'nl',
    'sv': 'sv',
    'da': 'da',
    'no': 'no',
    'fi': 'fi',
    'pt_BR': 'pt_BR',
    'pt_PT': 'pt_PT',
    'hu': 'hu',
    'eo': 'eo',
    'ru': 'ru',
    'bg': 'bg',
    'sr': 'sr',
    'uk': 'uk',
    'cs': 'cs',
    'sk': 'sk',
    'pl': 'pl',
    'ro': 'ro',
    'sl': 'sl',

