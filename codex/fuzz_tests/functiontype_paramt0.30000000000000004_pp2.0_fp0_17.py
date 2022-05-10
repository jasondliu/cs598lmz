from types import FunctionType
list(FunctionType(lambda: None, {}))

# Test __length_hint__
class LengthHint:
    def __length_hint__(self):
        return 42

list(LengthHint())

# Test __getitem__
class GetItem:
    def __getitem__(self, index):
        if index > 10:
            raise IndexError
        return index

list(GetItem())

# Test __iter__
class Iter:
    def __iter__(self):
        yield 1
        yield 2
        yield 3

list(Iter())

# Test __getitem__ and __len__
class GetItemLen:
    def __getitem__(self, index):
        if index > 10:
            raise IndexError
        return index

    def __len__(self):
        return 10

list(GetItemLen())

# Test __getitem__ and __iter__
class GetItemIter:
    def __getitem__(self, index):
        if index > 10:
            raise IndexError
        return index

    def __iter__(self):

