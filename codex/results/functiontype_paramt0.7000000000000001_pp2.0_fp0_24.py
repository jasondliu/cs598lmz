from types import FunctionType
list(FunctionType(f.__code__, globals(), '<lambda>', f.__defaults__, f.__closure__))

# use of lambda
# How many times does each letter appear in the following string:
s = 'This is a string of words.'

# solution:
s = 'This is a string of words.'
d = dict()
for letter in s:
    d.setdefault(letter, 0)
    d[letter] += 1

def count_letters(word):
    d = dict()
    for w in word:
        d.setdefault(w, 0)
        d[w] += 1
    return d

# use of lambda
# How many times does each letter appear in the following string:
s = 'This is a string of words.'

# solution:
s = 'This is a string of words.'
d = dict()
for letter in s:
    d.setdefault(letter, 0)
    d[letter] += 1

def count_letters(word):
    d = dict()
    for w in word:
        d.setdefault(
