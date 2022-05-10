from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), 'foo')(1))

# tp_richcompare
class C:
    def __eq__(self, other):
        return 1
    def __ne__(self, other):
        return 2
    def __lt__(self, other):
        return 3
    def __le__(self, other):
        return 4
    def __gt__(self, other):
        return 5
    def __ge__(self, other):
        return 6

c = C()
c == c
c != c
c < c
c <= c
c > c
c >= c

# tp_getattr, tp_getattro
class C:
    def __getattr__(self, name):
        return 1
    def __getattribute__(self, name):
        return 2

c = C()
c.x
c.x

class C:
    def __getattr__(self, name):
        return 1

c = C()
c.x

class C:
    def __get
