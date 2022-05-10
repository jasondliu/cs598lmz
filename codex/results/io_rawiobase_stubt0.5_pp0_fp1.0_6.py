import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename

    def read(self, size=-1):
        with open(self.filename, 'rb') as f:
            return f.read(size)

f = File('test.txt')
print(f.read())

# 方法2
# import io
# class File(io.BufferedIOBase):
#     def __init__(self, filename):
#         self.filename = filename

#     def read(self, size=-1):
#         with open(self.filename, 'rb') as f:
#             return f.read(size)

# f = File('test.txt')
# print(f.read())

# 方法3
# import io
# class File(io.TextIOBase):
#     def __init__(self, filename):
#         self.filename = filename

#     def read(self, size=-1):
#         with open(self.filename, 'r') as f:
#             return f.read(size)
