import sys, threading
threading.Thread(target=lambda:sys.stdout.write('hello\n'))
# At least one carriage return is needed to see the output on Windows
print()

# One more example.
class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

import keyword
if keyword.iskeyword('for'):
    print('for is a keyword')
else:
    print('for is not a keyword')

    # It is usually disconcerting to see a keyword used as an identifier. Raw literals are just strings.
    # In a raw literal, the backslash is just a backslash.

s = r'a\b\c'
print(s)

# Triple-quoted strings can span multiple lines
s = '''Finished files are the result of
    years of scientifc study combined with
    the experience of years'''
print(s)

s = """Finished files are the result
