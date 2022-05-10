import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def rand_func(x):
  return (x * (1 + (x * ((random.random() - 0.5)))) / 2.5)

def rand_func2(x):
  return (x * (1 + ((random.random() - 0.5) / 2.5)))

def rand_func3(x):
  return (x + (random.random() - 0.5) * x)

def rand_func4(x):
  return (x + (random.random() - 0.5) * x / 2.5)

def rand_func5(x):
  return (x + (random.random() - 0.5) * x * 2.5)

def rand_func6(x):
  return (x + (random.random() - 0.5) * x / 3.5)

def rand_func7(x):
  return (x + (random.random() - 0.5) * x * 3.5)

def rand_func8(x):
