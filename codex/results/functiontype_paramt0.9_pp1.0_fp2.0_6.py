from types import FunctionType
list(FunctionType(a(1), {}, "__main__", (), (), <module '__main__' (built-in)>).__globals__.items()) 
#['__loader__', 'exec', '__package__', '__spec__', '__doc__', '__annotations__', '__builtins__', 're', '__name__', 'quit', 'print', 'range', '__builtin__', 'a']
len(b(1)()())()()()()()()()()()()()()()()())
#11
c()
#<type 'list'>
d()
#[{'__builtins__': <module '__builtin__' (built-in)>, 'a': <function <lambda> at 0x03246710>, '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, 're': <module 're' from 'C:\\Users\\sosor\\AppData\\Local\\Programs\\Python\\Python35\\lib\\re.py'>, 'd':
