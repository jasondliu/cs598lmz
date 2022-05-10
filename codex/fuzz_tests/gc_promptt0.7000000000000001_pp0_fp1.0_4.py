import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:

    def __del__(self):
        print("in A.__del__()")

a = A()
print("1")
del a
print("2")
gc.collect()
print("3")
a = A()
print("4")
a = None
print("5")
gc.collect()
print("6")

# Test gc.get_referents()

class Node:

    def __init__(self, val):
        self.val = val
        self.children = []

    def add(self, x):
        self.children.append(x)

    def dump(self, x):
        self.dump_indent(x, 0)

    def dump_indent(self, x, indent):
        if x is not None:
            print(" "*indent, x.val)
            for y in x.children:
                self.dump_indent(y, indent+1)

    def __del__(self):
        print("in Node.__del__()")

root = Node("
