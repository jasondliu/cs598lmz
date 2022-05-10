import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
gc.collect()
gc.collect()
print()

# 测试gc.garbage
gc.collect()
print(gc.garbage)

class Graph:
    def __init__(self, name):
        self.name = name
        self.other = None
    def set_other(self, other):
        print('Connecting', self, 'to', other)
        self.other = other
    def __repr__(self):
        return 'Graph({})'.format(self.name)

print()
# 测试gc.get_objects()
gc.get_objects()

print()
# 测试gc.get_referrers()
gc.get_referrers()

print()
# 测试gc.get_referents()
gc.get_referents()

print()
# 测试gc.is_tracked()
gc.is_tracked()

print()
# 测试gc.set_threshold()
gc.set_threshold
