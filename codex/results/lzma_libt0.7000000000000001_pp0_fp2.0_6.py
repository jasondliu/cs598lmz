import lzma
lzma.decompress(lzma.compress(b'a' * 100000))

del lzma

# Cannot open lzma.so, so an ImportError is the expected behavior
import lzma

# =====================================================================
# Cleanup
# =====================================================================

del sys
del os
del time
del imp
del types

# Clear modules loaded by this test.
for modname in sys.modules.keys():
    if modname.startswith('test.'):
        del sys.modules[modname]

import gc

gc.collect()
assert not gc.garbage
gc.collect()
assert not gc.garbage

# =====================================================================
# Done
# =====================================================================

print('Test passed.')
