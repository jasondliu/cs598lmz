import weakref
# Test weakref.ref
[wr() for wr in [weakref.ref(i) for i in range(5)]]

for obj in [1, 2]:
    if obj is None:
        pass
