fn = lambda: None
gi = (i for i in ())
fn.__code__ = rela_1_if_b
print(fn.__code__)  # <code object <module> at 0x1053c7120, file "", line 0>

import dis
dis.dis(fn)
# 0 LOAD_DEREF              1 (i)
# 2 RETURN_VALUE

# it's rough translation:
#         LOAD_DEREF  1
#  -->    LOAD_CONST  1
#         RETURN_VALUE
