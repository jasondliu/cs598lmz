from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

import bz2
bz2.decompress(data)
```

题目中为什么要通过getinfo()来获取comment呢？当然是要骗我们。这个信息根本没有存储在BZ2压缩包里面。所以经过上面几个方法都不能完成题目要求。如何解决呢？我们只要自定义BZ2Decompressor的comment属性即可。什么是自定义呢？简单来说就是改变成我们想要的信息
