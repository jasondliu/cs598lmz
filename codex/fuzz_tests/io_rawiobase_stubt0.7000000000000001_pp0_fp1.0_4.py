import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='rb'):
        self.file = open(filename, mode)

    def close(self):
        return self.file.close()

    def fileno(self):
        return self.file.fileno()

x = File('../data/iris.csv')

print(x.read())
print(x.read(2))
print(x.read(2))
print(x.read(3))
print(x.read(4))
print(x.read(4))
print(x.read(4))
print(x.read(4))
print(x.read(4))


x.close()

#   with open('../data/iris.csv') as f:
#       print(f.read())
#
#   with open('../data/iris.csv') as f:
#       while True:
#           chunk = f.read(3)
#           if chunk:
#               print(chunk)
#           else:
#               break
#
#   with open('../data/
