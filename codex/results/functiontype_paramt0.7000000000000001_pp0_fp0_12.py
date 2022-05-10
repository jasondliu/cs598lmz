from types import FunctionType
list(FunctionType(a).__globals__.keys())

a = '''def a():
    pass
'''

def a():
    pass
print(a)
