import weakref
# Test weakref.ref():
s1 = {1, 2, 3}
def bye():
    print('Gone with the wind...')
ender = weakref.finalize(s1, bye)
ender.alive
del s1
ender.alive

# Test weakref.WeakKeyDictionary():
class Cheese:
    def __init__(self, kind):
        self.kind = kind
    def __repr__(self):
        return 'Cheese(%r)' % self.kind

stock = weakref.WeakKeyDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan'),]
for cheese in catalog:
    stock[cheese] = cheese.kind
