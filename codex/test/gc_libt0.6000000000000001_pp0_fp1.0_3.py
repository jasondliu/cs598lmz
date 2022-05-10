import gc, weakref

def my_dest(obj):
    print('my_dest', obj)

wr = weakref.ref(gc.collect, my_dest)

print(gc.collect())
print(wr)
print(gc.collect())
print(wr)

