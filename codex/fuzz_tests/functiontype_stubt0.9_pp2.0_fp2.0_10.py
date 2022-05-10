from types import FunctionType
a = (x for x in [1])
type(a)

def task():
    return 1

type(task) == FunctionType


# 迭代
class Node:

    def __init__(self):
        self.dataset = [1,2,3,4,5]

class Iterator:

    def __init__(self, index=0):
        self.index = index

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 4:
            raise StopIteration

        value = self.index
        self.index += 1
        return value

class NewNodeIter:

    def __init__(self, index=0):
        self.index = index

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 4:
            raise StopIteration

        value = self.index
        self.index += 1
        return value

class CatchNode:

    def __init__(self, dataset):
        self.data_set = dataset

    def __
