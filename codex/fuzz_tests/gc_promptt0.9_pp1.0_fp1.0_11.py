import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
while 1:
  with gc.garbage:
      print ("debe haber uno")
   
    #*ERROR* 8.py:20: cannot override readonly attribute
    #*WARNING* 7.py:18: Expected an indented block (syntax
    #  error)

##     print ("one or more!")
##   print ("no more!")
gc.collect()
print ("bye!")
