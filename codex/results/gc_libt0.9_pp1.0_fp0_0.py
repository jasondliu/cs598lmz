import gc, weakref

class A:
  def __del__(self):
    print ("A.__del__")

# Note that this takes effect after GC
gc.callbacks.append(lambda *args: print (args))

a = A()
w = weakref.ref(a)

print(w)
# '<weakref at 0x00000000028B1BF8; to 'A' at 0x00000000028B1CC8>'

del a
gc.collect()

print(w())
# 'None'

print(w)
# '<weakref at 0x00000000028B1BF8; dead>'

gc.collect()

# 0 (<weakref at 0x00000000028B1BF8; dead>, {<class '__main__.A'>: <function A.__del__ at 0x000000000259D598>})

# {'<weakref at 0x00000000028B1BF8; dead>'} 1

# {'<weakref at 0x00000000028B1BF8; dead>'} 2


