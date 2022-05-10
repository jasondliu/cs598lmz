import ctypes
ctypes.cast(1, ctypes.c_char)

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()

# Local Variables:
# compile-command: ";;; (eval-buffer) (save-buffer) (py-isort-buffer)"
# End:
