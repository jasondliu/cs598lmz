import ctypes

class S(ctypes.Structure):
    x = ctypes.c_wintypes.WCHAR
    y = ctypes.c_wintypes.WCHAR

def main():
    u1 = unichr(65)
    s = S(u1, u1)
    # _next_ is needed to prevent the compiler from caching the result of unichr().
    # This test fails if the compiler caches the result of unichr().
    u2 = _next_(u1)
    s.y  = u2
    s.x = u2
    
    if s.x != u2 or s.y != u2:
        raise RuntimeError("_next_ failed.")

if __name__ == "__main__":
    main()
