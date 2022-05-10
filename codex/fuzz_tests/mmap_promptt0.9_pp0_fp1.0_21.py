import mmap
# Test mmap.mmap
# https://docs.python.org/2/library/mmap.html

example = mmap.mmap(-1, 1000)
example[:2] = "\xff\xff";
example.seek(0);
print example.read(2);
example.close()
  

# Test a dictionary stored in a mmap object
d = shelve.open(filename='mydata')
d['one'] = "This is the first line"
d['two'] = "This is the second line"
print d['one']
print d['two']

for k, v in sorted(d.iteritems()):
    print '%s: %s' % (k, v)

d.close()

# https://docs.python.org/2/library/anydbm.html
import anydbm
db = anydbm.open(filename='tester', flag='n', mode=0666)
db['key'] = 'value'
print db['key']
print db.keys()
db.close()
