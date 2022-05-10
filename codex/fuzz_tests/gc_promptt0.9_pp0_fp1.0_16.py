import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage with weakrefs (bug #1021218)
class C:
	def __del__(self):
		print('deleting', self)
		self.callback()
		print('done')
	def __repr__(self):
		return 'C()'
def callback(wr):
	print('callback', self, wr, gc.collect(), gc.garbage)
	gc.garbage.remove(wr)
	print('callback ->', gc.collect(), gc.garbage)
c = C()
c.callback = callback
wref = weakref.ref(c, callback)
del c
gc.garbage.append(wref)
print(len(gc.garbage), gc.garbage[0]())
print('collect', gc.collect())
print('#' * 23)
