from _struct import Struct
s = Struct.__new__(Struct)
flags = []
flags.insert(0, '@')
flags.insert(1, '')
for index, char in enumerate('bBhHiIlLqQfdfd'):
    flags.append(str(char))
    s.format = ''.join(flags)
    print s.size
    flags.pop()
