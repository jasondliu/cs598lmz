from types import FunctionType
list(FunctionType(lambda: None))

# Test __repr__
class A:
    def __repr__(self):
        return "A()"

class B:
    def __repr__(self):
        return "B()"

list(A())
list(B())

# Test __getitem__
class C:
    def __getitem__(self, key):
        return key

class D:
    def __getitem__(self, key):
        return key

list(C())
list(D())

# Test __iter__
class E:
    def __iter__(self):
        return iter([1, 2, 3])

class F:
    def __iter__(self):
        return iter([1, 2, 3])

list(E())
list(F())

# Test __len__
class G:
    def __len__(self):
        return 3

class H:
    def __len__(self):
        return 3

list(G())
list(H())

# Test __contains__

