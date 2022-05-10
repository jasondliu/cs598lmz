import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Import the email modules we'll need
from email.parser import Parser

# If the e-mail headers are in a file, uncomment these two lines:
# with open(messagefile, 'r') as fp:
#     headers = Parser().parse(fp)

# Or for parsing headers in a string, use:
headers = Parser().parsestr('From: <user@example.com>\n'
                            'To: <someone_else@example.com>\n'
                            'Subject: Test message\n'
                            '\n'
                            'Body would go here\n')

# Now the header items can be accessed as a dictionary:
print('To: {}'.format(headers['to']))
print('From: {}'.format(headers['from']))
print('Subject: {}'.format(headers['subject']))

# Or you can use the email.message module to walk through the parts of the
# message.  The walk method of the EmailMessage class returns a generator
# object that allows you
