fn = lambda: None
# Test fn.__code__.co_varnames
# Test fn.__code__.co_argcount


# 2.5.5
# Read and write from StringIO

import StringIO

buffer = StringIO.StringIO()
buffer.write('This is a test\n')
buffer.write('This is another test\n')

print 'This is the buffer:', buffer.getvalue()
buffer.close()

# 2.5.6
# Read and write from cStringIO

import cStringIO

buffer = cStringIO.StringIO()
buffer.write('This is a test\n')
buffer.write('This is another test\n')

print 'This is the buffer:', buffer.getvalue()
buffer.close()

# 2.5.7
# Import by name

import moduletest
moduletest.myfunc()

# 2.5.8
# findall

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print y

# 2.5.9
