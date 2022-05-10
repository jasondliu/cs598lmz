import weakref
# Test weakref.ref(n) == weakref.ref(n) for all nodes.
assert all(weakref.ref(n) == weakref.ref(n) for n in nodes)
# Test weakref.ref(n) == weakref.ref(m) only for n == m.
assert sum(1 for n in nodes
           for m in nodes
           if n != m and weakref.ref(n) == weakref.ref(m)) == 0
# Test weakref.ref(n) != weakref.ref(m) for all n != m.
assert all(weakref.ref(n) != weakref.ref(m) for n in nodes
           for m in nodes if n != m)
# Test weakref.ref(n) != weakref.ref(m) for all n != m.
assert all(weakref.ref(n) != weakref.ref(m) for n in nodes
           for m in nodes if n != m)
# Test weakref.ref(n) is weakref.ref(n) for all n.
