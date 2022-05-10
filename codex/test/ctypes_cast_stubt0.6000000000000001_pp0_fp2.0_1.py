import ctypes
ctypes.cast(0, ctypes.py_object)

# -----------------------------

# 扩展类型

class MyList(list):
    def __getitem__(self, offset):
        print('(indexing %s at %s)' % (self, offset))
        return list.__getitem__(self, offset - 1)

if __name__ == '__main__':
    print(list('abc'))
    x = MyList('abc')
    print(x)

    print(x[1])
    print(x[3])
    x.append('spam'); print(x)
    x.reverse(); print(x)

    class MyList(list):
        def __getitem__(self, index):
            if index == 0: raise IndexError
            if index > 0: index = index - 1
            return list.__getitem__(self, index)

        def __setitem__(self, index, value):
            if index == 0: raise IndexError
            if index > 0: index = index - 1
