from types import FunctionType
list(FunctionType(lambda:1,{},None,None,None))
#[1]
def f():yield 1
list(f())
#[1]
list(f())
#[]
list(f())
#[]
def f():yield 1
f().next()
#1
f().next()
#StopIteration
g=f()
g.next()
#1
g.next()
#StopIteration
def f():
  for i in range(3):
    yield i
list(f())
#[0, 1, 2]
def f():
  for i in range(3):
    if i==1:
      return
    yield i
list(f())
#[0]
def f():
  for i in range(3):
    if i==1:
      break
    yield i
list(f())
#[0]
def f():
  for i in range(3):
    if i==1:
      continue
    yield i
list(f())
#[0, 2]
def f():
  for i in range(3):
