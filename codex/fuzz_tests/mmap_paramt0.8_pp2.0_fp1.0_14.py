import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 50
</code>
I'd like to know if it's possible to have a property of a python class that would point to such an mmap object, such that I can do:
<code>my_object.my_property[0] = "some new value"
</code>
I tried doing:
<code>with open('test', 'r+b') as f:
    self.__m = mmap.mmap(f.fileno(), 0)

@property
def my_property(self):
    return self.__m
</code>
but it doesn't seem to work. Any ideas?


A:

I don't know how sensible this is, but you could just make it a separate method:
<code>self.__m = mmap.mmap(f.fileno(), 0)

def my_property(self, i, v=None):
    if v is None:
        return self.__m[i]
    else:
        self.__m[i] = v
        return v
</code>
Then you can do
