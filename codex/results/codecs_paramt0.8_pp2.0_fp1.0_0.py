import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Shortcut
I18n = TranslationString

# ------------------
# String interpolation
#  https://stackoverflow.com/a/11276687/1350289
# ------------------
# See https://github.com/Pylons/pyramid/wiki/Introspecting-your-application-for-i18n-messages
# for a way to maintain the source strings without having to write it twice.
#
# For example, _("hello %s") % ("world",) will give you a TranslationString
# containing the string "hello %s". It is also possible to use *args (for
# positional arguments) and **kwargs (for named arguments). If a format
# string is passed in as a named argument (ex: %("foo")) then this string
# will be i18n'ed as well.

_ = TranslationString
_plural = PluralTranslate

# ------------------
# Date interpolation
# ------------------

_date_patterns = {
    'fuzzy': {
        'today': _("
