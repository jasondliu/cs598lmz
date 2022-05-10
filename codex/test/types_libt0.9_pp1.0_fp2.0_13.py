import types
types.MethodType(f, None, Spam)

class Spam:
    count = 0
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '[Spam {}]'.format(self.name)


    def show(self):
        print('Instance {} ({})'.format(self.name, self.count))

class Sub(Spam):
    def __init__(self, name):
        Spam.__init__(self, name)

    def action(self):
        print(self.name.upper())

b = Spam('Guido')
S = Sub('bob')
S.show()
S.action()
b.count
print(b.name)
b.name = 'Bob'
print(b.name)
Spam.count = 1
print(b.count)
b.count = 2
print(b.count)
print(Spam.count)
d = Spam('mel')
