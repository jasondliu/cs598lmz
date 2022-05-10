import weakref
# Test weakref.ref() for objects with a custom __hash__ method.

class Test:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return self.value

class Test2(Test):
    def __eq__(self, other):
        return self.value == other.value

class Test3(Test):
    def __hash__(self):
        return Test.__hash__(self)

class Test4(Test):
    def __hash__(self):
        return Test.__hash__(self)

    def __eq__(self, other):
        return self.value == other.value

class Test5(Test):
    def __hash__(self):
        return Test.__hash__(self)

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

class Test6(Test):
    def __hash__(self):
        return Test.__hash__(self)

   
