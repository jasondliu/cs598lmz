import types
# Test types.FunctionType
def te():
  return 0

def teea():
  return

#def tes():
#  "ABC"
#  return
def test(level=1):
  APP = level
  if APP == 1:
    # Test types.LambdaType
    te1 = (lambda:0)
  def te2(l):
    return l
    #return 0
  out1 = (0 for a in range(4))
  # Test type(fs) == types.GeneratorType
  try:
    if True:
      out2 = (te2(a) for a in range(4))
      out3 = {a:te2(a) for a in range(4)}
      out4 = {te2(a) for a in range(4)}
    else:
      out2 = (te2(a) for a in range(4))
      out3 = {a:te2(a) for a in range(4)}
      out4 = {te2(a) for a in range(4)}
  except:
    pass
  # Test
