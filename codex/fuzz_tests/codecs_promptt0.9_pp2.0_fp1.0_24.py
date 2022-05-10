import codecs
# Test codecs.register_error function
#

import codecs
import locale
import string

f = codecs.open('Blowing from the West.html', 'r', encoding='utf8', errors='bad_escape')
for line in f:
    if string.find(line, u'\ufffa') >= 0:
        print 'Error found'
        break
else:
    print 'No error found'
try:
    u = line.encode('latin1')
except UnicodeEncodeError, err:
    print 'EncodeError'
    print err.args[1]
else:
    print 'No EncodeError'
