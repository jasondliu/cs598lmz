import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int),ctypes.c_int)


@FUNTYPE
def callfun(p,n):
    p = list(p.contents)
    index = 0
    while(index&lt;n):
        print(p[index])
        index = index + 1
    return 0
</code>
My compiled object file is:
<code>00000000 &lt;callfun&gt;:
   0:   55                      push   %ebp
   1:   89 e5                   mov    %esp,%ebp
   3:   53                      push   %ebx
   4:   83 ec 20                sub    $0x20,%esp
   7:   8b 45 08                mov    0x8(%ebp),%eax
   a:   8b 00                   mov    (%eax),%eax
   c:   83 c0 04                add    $0x4,%eax
   f:   83 ea 01                sub    $0x1,%edx
  12:
