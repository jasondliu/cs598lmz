import codecs
codecs.register_error('strict', codecs.ignore_errors)

# the file is encoded in cp1252, but it contains some invalid cp1252 characters
# (the Euro sign and some control characters)
# we use utf-8 as a replacement encoding, since it can represent all characters
# in the file

with open('cp1252.txt', encoding='cp1252', errors='strict') as infile:
    data = infile.read()

with open('utf-8.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(data)
</code>
Now, if you view the <code>cp1252.txt</code> file in Notepad, you will see a bunch of <code>?</code> characters.  If you view the <code>utf-8.txt</code> file in Notepad, you will see the Euro symbol and the control characters.

