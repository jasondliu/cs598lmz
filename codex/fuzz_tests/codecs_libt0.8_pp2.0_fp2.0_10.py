import codecs
codecs.BOM_UTF8.decode('utf-8')

import os
os.environ.get('PYTHONIOENCODING')

os.environ.get('PYTHONIOENCODING', 'utf-8')


# On Windows, this is the ANSI code page for the locale; on other platforms, it's always UTF-8.
# To use a different encoding in Python scripts on Windows, change the PYTHONIOENCODING environment variable.
# For example:
# set PYTHONIOENCODING=cp1252

## 4.17. Output Formatting

# See also: The string format() method, str.format(), and Formatter

# The str.format() method of strings requires more manual effort
# str.format() allows greater control over formatting

#print('We are the {} who say "{}!"'.format('knights', 'Ni'))
#print('{0} and {1}'.format('spam', 'eggs'))
#print('{1} and {0}'.format('spam', 'eggs'))
