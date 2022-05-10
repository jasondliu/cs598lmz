import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
</code>
This gives me <code>ReferenceError: weakly-referenced object no longer exists</code> when <code>del f</code> is called, which is not surprising. I have been doing some research and found out that Python uses reference counting to keep track of objects and also a reference cycle detector to detect cycles in Python objects. 
The reference cycle detector uses a simple mark and sweep algorithm to detect cycles and then breaks them by setting the object's reference to <code>None</code>. So the documentation says, <code>"That the reference count drops to zero is the normal case for most objects; for objects participating in reference cycles, the cyclic garbage detector may break the cycles and the reference count may drop to zero during the process. In either case, the object’s memory is freed. Cyclic garbage detection occurs during the following operations: when an object’s reference count drops to zero; when a very long list of objects is created; when a module is deleted, typically when its program is finished."</code>
The problem here is that the reference cycle detector is not invoked because the reference count of my <code>f</code> object is still 1 even though <
