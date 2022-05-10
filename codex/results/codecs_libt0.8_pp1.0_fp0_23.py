import codecs
codecs.open('file.txt', encoding='utf-8')

# If a file is opened with the mode 'rU', it will be opened as if UTF-8 encoding was used.
# This occurs because the 'U' mode doesn't exist and is interpreted as 'r' and 'U'.
# This doesn't have any effect on the behaviour of the file, except that it will treat it as UTF-8 encoded.
codecs.open('file.txt', encoding='utf-8', mode='rU')

# Open a  file as an UTF-8 encoded file.
codecs.open('file.txt', mode='r', encoding='utf-8')

# Open a  file as an UTF-16 encoded file.
codecs.open('file.txt', mode='r', encoding='utf-16')

# The 'encoding' argument is the preferred way to specify the encoding.
f = codecs.open('file.txt', encoding='utf-8')

# The 'fileencoding' argument is an alias for 'encoding'
f = codecs.open('file.txt', fileencoding
