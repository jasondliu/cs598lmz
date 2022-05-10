import types
types.new_class('Foo', (), {'__slots__': ('bar',)})
# end::MUTABLE_TYPES_CUSTOM_CLASS[]

# tag::MUTABLE_TYPES_WEAK_REFERENCE[]
import weakref
class Bar: pass
o = Bar()
weakref.ref(o)
# end::MUTABLE_TYPES_WEAK_REFERENCE[]

# tag::MUTABLE_TYPES_WEAK_KEY_DICTIONARY[]
import weakref
class Bar: pass
o = Bar()
d = weakref.WeakKeyDictionary()
d[o] = 'foo'
# end::MUTABLE_TYPES_WEAK_KEY_DICTIONARY[]

# tag::MUTABLE_TYPES_WEAK_VALUE_DICTIONARY[]
import weakref
class Bar: pass
o = Bar()
d = weakref.WeakValueDictionary()
d[0] = o
# end::MUTABLE_TYPES_WEAK_VALUE_DICTIONARY[]
