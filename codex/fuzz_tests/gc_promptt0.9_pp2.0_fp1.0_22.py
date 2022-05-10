import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() (no arguments)
gc.collect()


class NewStyle(object):
    pass

class Classic:
    pass

class FinalizedClassic:
    __slots__ = ()

    def __del__(self):
        pass

class NewStyleDerived(NewStyle):
    pass

class ClassicDerived(Classic):
    pass


instances = [Classic(), NewStyle(), ClassicDerived(), NewStyleDerived()]
for c in (Classic, NewStyle, ClassicDerived, NewStyleDerived):
    instances.append(c.__new__(c))
for i in instances:
    print(gc.is_tracked(i), gc.is_tracked(i, memoryview(b"foo")))

weak_refs_instances = [weakref.ref(i) for i in instances]
for i in instances:
    print(gc.is_tracked(i), gc.is_tracked(i, memoryview(b"foo")))
for i in weak_refs_instances:
    if i() is not None:

