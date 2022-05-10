fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #17091: test that the code object is not freed before the generator
# iterator is freed.
import gc
gc.collect()

# Issue #17091: test that the code object is not freed before the generator
# iterator is freed.
import gc
gc.collect()

# Issue #17091: test that the code object is not freed before the generator
# iterator is freed.
import gc
gc.collect()

# Issue #17091: test that the code object is not freed before the generator
# iterator is freed.
import gc
gc.collect()

# Issue #17091: test that the code object is not freed before the generator
# iterator is freed.
import gc
gc.collect()

# Issue #17091: test that the code object is not freed before the generator
# iterator is freed.
import gc
gc.collect()

# Issue #17091: test that the code object is not freed before the generator
# iterator is freed.
import gc
gc.collect()

# Issue #
