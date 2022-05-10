import ctypes
ctypes.cast(buf, ctypes.POINTER(ctypes.c_ubyte)).contents

import clr
clr.AddReference("System.Numerics")
types = [
    clr.LoadAssemblyFromFileWithPath("TestUnmanagedTypeAttribute.dll"),
    clr.LoadAssemblyFromFileWithPath("TestUnmanagedTypeAttribute.dll"),
    clr.LoadAssemblyFromFileWithPath("TestUnmanagedTypeAttributeAssembly.dll"),
]

# unPrefixed
for type in types:
    ass = System.Reflection.Assembly.Load(type)
    for t in ass.GetTypes():
        if getattr(t, "__unmanaged__", None):
            print t
            continue

        if t.FullName in ["TestUnmanagedTypeAttribute.UnmanagedInt",
                          "TestUnmanagedTypeAttribute.UnmanagedInt2",
                          "TestUnmanagedTypeAttributeAssembly.UnmanagedInt3"]:
            print t, getattr(t, "__unmanaged__", None)

# prefixed
for type in types:
    ass = System.Reflection.Assembly.
