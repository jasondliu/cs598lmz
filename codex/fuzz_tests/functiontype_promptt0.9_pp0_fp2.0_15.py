import types
# Test types.FunctionType objects
class TFoo:
  def bar (self): pass
  f = bar
inst = TFoo ()
inst.f () # invoke instance method
TFoo.f (inst) # Instance is passed by manual dispatch
# Same instance method, but now accessed as a different method
TFoo.f2 = TFoo.f
inst.f2 () # invoke instance method (as f2)
# Same again, but now accessed as a function
TFoo.f3 = TFoo.f.im_func
TFoo.f3 (inst) # invoke instance method (as f3)

# This piece of code is inserted by the compiler
def fstep_next_step(fstep):
  if fstep.f_exc_type is not None:
    raise fstep.f_exc_type, fstep.f_exc_value
  return fstep.f_locals.get(fstep.var, None)

# This piece of code is inserted by the compiler
fstep_next = fstep_next_step
fstep = types.FunctionType(
  0, globals(), None, '
