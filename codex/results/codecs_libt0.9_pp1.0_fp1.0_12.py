import codecs
codecs.getdecoder('rot_13')('abc')
d = {'a': 'z', 'b': '3'}
d['b']
d['x']
d.get('x')
d.get('x', 'y')
d.get('x', 'X not in dict')
 
 
del d['a']
d['a']
d.keys()
 
d.values()
list(d.values())
 
set(d.values())
list(d.items())
for k, v in d.items():
    print('key=%s, value=%s' % (k, v))
 
d2 = {'y': '9', 'x': '1'}
d.update(d2)
d
 
d2.update(d)
d2
def copies2(string, times):
    new_str = str()
    for i in range(times):
        new_str += string
    return new_str
 
def copies3(string, times):
    return string * times
 
 
def
