from types import FunctionType
list(FunctionType(lambda:0,{},None,None,None))

# Test the list() function on a function object with a __getitem__ method
# (this is the case for the function object itself)
list(list)

# Test the list() function on a function object with a __getitem__ method
# (this is the case for the function object itself)
list(list)

# Test the list() function on an object with a __getitem__ method that
# raises an exception other than IndexError
class SequenceWithoutGetItem(object):
    def __len__(self):
        return 4
    def __getitem__(self, i):
        if i == 2:
            raise ValueError
        return i

list(SequenceWithoutGetItem())

# Test the list() function on an object with a __getitem__ method that
# raises StopIteration
class SequenceWithBadGetItem(object):
    def __getitem__(self, i):
        if i == 2:
            raise StopIteration
        return i

list(SequenceWithBadGetItem())

# Test the list
