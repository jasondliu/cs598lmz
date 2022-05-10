import ctypes
ctypes.CDLL("./example.so", mode=ctypes.RTLD_GLOBAL)
import example

print(example.add(4,5))
print(example.sub(4,5))
</code>
Output:
<code>9
-1
</code>

