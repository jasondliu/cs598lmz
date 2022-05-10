from types import FunctionType
a = (x for x in [1])
b = [1]

print type(a)
print type(b)

c = FunctionType
#print c.__getattribute__
#print a.__getattribute__
dic1 = {'name':'lizhiqiang','age':18}
dic2 = {'name':'lisisi','age':20}
def where(obj):
    return obj.get('name') == 'lizhiqiang'
for i in filter(where, [dic1,dic2]):
    print i
class B(dict):
    def __getattribute__(self, *args, **kwargs):
        v = super(B,self).__getattribute__(*args, **kwargs)
        print 'class'
        return v

    def __getitem__(self, item):
        v = super(B,self).__getitem__(item)
        return v+1

obj = B()
obj['k'] = 1
print obj['k']
print obj.get('k')
print obj.get
print obj.get('name')

