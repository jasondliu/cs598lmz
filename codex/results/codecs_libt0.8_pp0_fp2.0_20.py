import codecs
codecs.open('C:/Users/MAIN/Documents/Data Science/Machine Learning/log1.txt', 'r', encoding='utf-8')

# Or, use a few different methods to handle UTF-8 strings:

# StringIO, BytesIO and StringIO can be used to work with Unicode strings
import StringIO
import cStringIO

# Use the cStringIO.StringIO class for working with text (UTF-8)
s = StringIO.StringIO(u'Hello\nWorld\n')
s = cStringIO.StringIO(u'Hello\nWorld\n')
# Use the StringIO.BytesIO class for binary data
b = StringIO.BytesIO(u'Hello\nWorld\n')
# Use the unicode() built-in function for converting to Unicode
unicode(b.read(), 'utf-8')

# Here is an example that reads text from a file, translates all
# non-ascii characters to '?' using the unicode() built-in function
# and then writes the results back to a file.

#Write a Unicode string to a file
with
