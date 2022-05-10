from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
print(s.size)

# The standard library contains a number of modules providing access to system
# functionality, such as os. The os module offers an external file system
# interface, while a second module, shutil, provides a high-level interface to
# filesystem operations such as copying or deletion.

# Let's say you need to know how much free space is available on your system.
# The answer depends on the underlying operatio
