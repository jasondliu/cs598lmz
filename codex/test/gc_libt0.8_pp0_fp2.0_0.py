import gc, weakref

class ClassC(object):
    pass

class ClassB(object):
    pass

class ClassA(object):
    pass

class ClassD(object):
    pass

children = []
children.append(ClassA())
children.append(ClassB())
children.append(ClassC())
d = ClassD()
d.children = children

del children
