import weakref
# Test weakref.ref() and weakref.ReferenceType().
print_doc(weakref.ref)

# Test weakref.proxy() and weakref.ProxyType().
print_doc(weakref.proxy)

# Test weakref.getweakrefcount() and weakref.getweakrefs().
print_doc(weakref.getweakrefcount)
print_doc(weakref.getweakrefs)


# Test weakref.WeakKeyDictionary.
print_doc(weakref.WeakKeyDictionary)
# Test weakref.WeakValueDictionary.
print_doc(weakref.WeakValueDictionary)
