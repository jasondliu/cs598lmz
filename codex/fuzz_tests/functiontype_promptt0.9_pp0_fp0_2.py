import types
# Test types.FunctionType
type(chr)

import string
# Test string.
# The string module contains multiple types of alphabets, punctuation, and digits.
# Test string.ascii_lowercase
string.ascii_lowercase
string.punctuation

list(string.whitespace)

P = '''
X= input('Enter anything: ')
Y= len(X)
print(Y)
'''

def read_code(filename):
    with open(filename) as f:
        # Test f.readlines()
        # it returns list of lines
        lines = f.readlines()
        # Test string.join()
        return ''.join(lines)

file_name = 'test_read_code.txt'
with open(file_name, 'w') as fw:
    fw.write(P)

# test os.path.isfile()
os.path.isfile(file_name)

read_code(file_name)

# test os.remove()
os.remove(file_name)


