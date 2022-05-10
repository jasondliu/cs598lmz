import gc, weakref

s = set()

for i, ref in enumerate(gc.get_referrers(s)):
    if isinstance(ref, weakref.ref):
        print(i, 'ref', ref)
        print(i, 'ref().__class__.__name__', ref().__class__.__name__)
        print(i, 'type(ref().__class__.__name__', type(ref().__class__.__name__))
    else:
        print(i, 'ref', ref)
        print(
            i,
            'type(ref)',
            type(ref))
