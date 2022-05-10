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

print(view)
</code>

<code>&lt;memory at 0x000002B8B1B6FB68&gt;
</code>
Is there something like <code>sys.getrefcount</code> for internal c++ memory ?


A:

When an object is created, it's not just the Python object that's created, you also allocate the object's <code>PyVarObject</code> header, which is a type-specific header (for example, this header __Pyx_TypeTest("str", x) would only be allocated for strings), the Python object's dictionary, and a reference to the type (the type is always present, and there's no way to remove it).
The <code>PyVarObject</code> header will often have a few or even several references (I don't know whether it's a hard rule or not), while the dictionary always has precisely one. The dictionary may have more references in some cases (if it's updated, if it has values that are strings that are interned, etc.), but there's no case where the dictionary has nearly as many references as the object.
I'd recommend reading through
