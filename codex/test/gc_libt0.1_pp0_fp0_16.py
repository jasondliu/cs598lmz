import gc, weakref

class C(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(%s)' % self.name

def f():
    c1 = C('c1')
    c2 = C('c2')
    c3 = C('c3')
    c4 = C('c4')
    c5 = C('c5')
    c6 = C('c6')
    c7 = C('c7')
    c8 = C('c8')
    c9 = C('c9')
    c10 = C('c10')
    c11 = C('c11')
    c12 = C('c12')
    c13 = C('c13')
    c14 = C('c14')
    c15 = C('c15')
    c16 = C('c16')
    c17 = C('c17')
    c18 = C('c18')
    c19 = C('c19')
    c20 = C('c20')
   
