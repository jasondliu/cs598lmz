import types
# Test types.FunctionType
class A(object):
  pass
def pyth(x,y):
  return x*x + y*y
def rev(x,y):
  return y,x
def cls(x,y):
  return A()
# test properties
def get_x(self):
  return self.x
def set_x(self, x):
  self.x = x
def del_x(self):
  del self.x
def get_x2(self):
  return self.x
def set_x2(self, x):
  self.x = x
def del_x2(self):
  del self.x
def get_x3(self):
   return self.x
def set_x3(self, x):
   self.x = x
def del_x3(self):
   del self.x
def get_x4(self):
  return self.x
def set_x4(self, x):
  self.x = x
def del_x4(self):
  del self.x
def get_x5
