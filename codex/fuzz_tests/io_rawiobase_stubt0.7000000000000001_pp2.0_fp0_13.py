import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path

    def open(self, mode='r'):
        return open(self.path, mode)

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def write(self, content):
        with open(self.path, 'w') as f:
            return f.write(content)

# f = File('hello.txt')
# f.write("hello python")
# ret = f.read()
# print(ret)

class A:
    def __init__(self):
        self.name = 'A'

    def func(self):
        print("A")

class B:
    def __init__(self):
        self.name = 'B'

    def func(self):
        print("B")

class C(A, B):
    def __init__(self):
        super().__init__()
        self.name = 'C'

c = C()
print(c.name
