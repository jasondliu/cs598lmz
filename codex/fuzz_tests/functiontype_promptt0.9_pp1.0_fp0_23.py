import types
# Test types.FunctionType
def f1(s):
  print "f1 got s=",s
def f2(s):
  print "f2 got s=",s
class C1:
  def g1(self,s):
    print "C1.g1 got s=",s
  def g2(s,self):
    print "C1.g2 got s=",s
  def __call__(self,s):
    print "C1 got s=",s
c=C1()
for f in (f1,f2,c.g1,c.g2,c):
  it=iter(f)
  try:
    while 1:
      it.next()
  except TypeError:
    pass
  assert(type(f) is types.FunctionType)

# Test types.GeneratorType
def ggen():
  v=1
  while v<10:
    yield v
    v=v+1
  v=v+5
  yield v
def tgen():
  v=1
  while v<10:
    yield v
