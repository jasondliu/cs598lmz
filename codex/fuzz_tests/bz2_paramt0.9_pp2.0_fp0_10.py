from bz2 import BZ2Decompressor
BZ2Decompressor()
# >>>
# bz2.error: invalid logic initialisation; this is probably a bug in bz2 itself
```

So we need to figure out what BZ2 does that breaks our SSE2 _pmovmskb_.

I suspect we need to tell GCC that the instructions are "unsafe", but we can use
them anyway.

FIXME say how to actually do that.

As a possible workaround, instead of checking against
`static_cast<uint16_t>(std::numeric_limits<T>::max())` and `static_cast<T>(0)`,
we could check against `static_cast<uint16_t>(-1)`.

Reference: https://github.com/arximboldi/sse2neon/blob/master/sse2neon.h

### Architecture

https://stackoverflow.com/questions/1418015/how-to-detect-cpu-and-or-instruction-set-availability-at-runtime-in-x86-64

## Thread sanitizer

Pass `-fsanit
