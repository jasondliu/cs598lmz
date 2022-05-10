fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #26
import sys
sys.modules['sys'] = None
import sys

# Issue #27
import sys
sys.modules['sys'] = sys
import sys

# Issue #28
import sys
sys.modules['sys'] = sys
import sys

# Issue #29
import sys
sys.modules['sys'] = sys
import sys

# Issue #30
import sys
sys.modules['sys'] = sys
import sys

# Issue #31
import sys
sys.modules['sys'] = sys
import sys

# Issue #32
import sys
sys.modules['sys'] = sys
import sys

# Issue #33
import sys
sys.modules['sys'] = sys
import sys

# Issue #34
import sys
sys.modules['sys'] = sys
import sys

# Issue #35
import sys
sys.modules['sys'] = sys
import sys

# Issue #36
import sys
sys.modules['sys'] = sys
import sys

# Issue #37
import sys
sys.modules['sys'] = sys

