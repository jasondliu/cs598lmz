from types import FunctionType
list(FunctionType(lambda: print('ok'), None, '', (), None, None, '', '', 0, ''))

class Example(object):
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return '<{!r}>'.format(self.name)

def example():
  yield Example('a')
  yield Example('b')

def example2():
  yield Example('c')
  yield Example('d')

def example3():
  yield Example('e')
  yield Example('f')

def example4():
  yield Example('g')
  yield Example('h')

list(example())
list(example2())
list(example3())
list(example4())

list(Example('a'))
list(Example('b'))
list(Example('c'))
list(Example('d'))
list(Example('e'))
list(Example('f'))
list(Example('g'))
list(Example('h'))

def example5():
  yield Example
