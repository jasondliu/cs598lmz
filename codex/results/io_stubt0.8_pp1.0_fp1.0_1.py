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
del view

# Test crashers:
# test_core.py::(anonymous)::(var.contains)::core
# test_core.py::(anonymous)::(var.is_true)::core
# test_core.py::(anonymous)::(var.is_false)::core
# test_core.py::(anonymous)::(var.is_type)::core
# test_core.py::(anonymous)::(var.is_not_type)::core
# test_core.py::(anonymous)::(var.debug_eq)::core
# test_core.py::(anonymous)::(var.debug_neq)::core
# test_core.py::(anonymous)::(var.same_type)::core
# test_core.py::(anonymous)::(var.not_same_type)::core
# test_core.py::(anonymous)::(var.is_of_type)::core
# test_core.py::(anonymous)::(var.is_not_of_type)::core
# test
