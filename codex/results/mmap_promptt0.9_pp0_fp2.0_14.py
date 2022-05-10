import mmap
# Test mmap.mmap.read() vs mmap.read()
#
# mmap.mmap.read(1)
#   => doc says it returns a string
#   => but returns a number if a number is in the string (which is the ascii code)
# mmap.read(1)
#   => maybe a method that reads/prints 1 char at a time?

d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
# del_list = ['a', 'b', 'c', 'd', 'e']
del_list = ['a', 'b', 'c']

def p(s):
    print(s)

def del_dict(*args):
    for k in args:
        if k in d:
            del(d[k])


del_dict(del_list[1], del_list[2])
del_dict(*del_list)
# del_dict(*del_list)
print(d)
quit()
fo = open("file.txt", "r+")
map = mmap
