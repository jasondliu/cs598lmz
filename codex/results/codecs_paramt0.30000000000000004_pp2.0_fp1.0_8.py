import codecs
codecs.register_error('strict', codecs.ignore_errors)

# The following is a list of all the supported languages.
# The first element of each tuple is the language code,
# and the second element is the language name.
# The language code is used to name the directory in which the
# language-specific files are stored.  The language name is used
# in the title of the HTML page.
#
# The first language in the list is the default language.
#
# If you add a new language, you must also add a new directory
# for that language.  The directory name should be the same as
# the language code.  In that directory, you should add a file
# named "index.html" that contains the translated version of
# the main page.  You should also add a file named "strings.js"
# that contains the translations of the strings used in the
# JavaScript code.
#
# You should also add the language code to the list of languages
# in the file "strings.js".

LANGUAGES = [
    ('en', 'English'),
    ('es', 'Español'),
