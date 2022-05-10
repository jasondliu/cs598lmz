import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
try:while lst:keepali0e.append(lst[:])except:pass
'''

class WeakrefGenerator(MixedGenerator):
    def __init__(self):
        MixedGenerator.__init__(self)
        self.list_generator = ListGenerator(self)
        self.del_generator = DelGenerator(self)
        self.ref_generator = WeakrefGenerator(self)
        self.call_closure_generator = CallClosureGenerator(self)
        self.one_shot(self.list_generator)
    def run(self):
        try:
            MixedGenerator.run(self)
        except ReferenceError:
            pass

class CallClosureGenerator(DelGenerator):
    def __init__(self,parent):
        self.__parent = parent
        MixedGenerator.__init__(self)
        self.reverse_generator = ReverseGenerator(self)
        self.append_generator = AppendGenerator(self)
    def init(self):
        self.__parent
