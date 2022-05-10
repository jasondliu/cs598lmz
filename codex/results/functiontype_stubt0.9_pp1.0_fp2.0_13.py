from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
bb = zip(a,a)
print bb


print "test string"
test = '''test1test2test3
test1test2test3
'''
print test.strip()
num = raw_input()
if int(num) == 123:
    print "right"
else:
    print "wrong"
