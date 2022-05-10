import ctypes
# Test ctypes.CField instances
print ctypes.CField.__repr__.__doc__
print ctypes.CField.__getattribute__.__doc__
print ctypes.CField.__setattr__.__doc__
print ctypes.CField.__setattr__.__doc__
print ctypes.CField.__delattr__.__doc__
print ctypes.CField.__str__.__doc__
print ctypes.CField.__cmp__.__doc__
print ctypes.CField.__hash__.__doc__
print ctypes.CField.__init__.__doc__
print ctypes.CField.__new__.__doc__
print ctypes.CField.from_address.__doc__
print ctypes.CField.offset.__doc__
print ctypes.CField.size.__doc__
print ctypes.CField.name.__doc__


print ctypes.CField()

try:
    ctypes.CField.__repr__()
except TypeError, details:
    if not str(details).startswith("desc
