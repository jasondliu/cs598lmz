import types
types.ModuleType
assert type(len) == types.BuiltinFunctionType

# process for waitpid, pipe, getppid, spawnve
x = os.fork()
assert x == 0 or type(x) == type(1)

x = os.waitpid(x, 0)
assert type(x) == type((0,0))

# internal use
import gc
assert type(gc.garbage) == type([])
assert type(gc.get_stats()) == type({})
assert type(gc.get_threshold()) == type((0,0,0))

import imp
assert type(imp.get_suffixes()) == type([])
assert type(imp.get_tag()) == type('')
assert type(imp.get_magic()) == type('')

assert type(imp.lock_held()) == type(0)
assert type(imp.lock_held(1)) == type(0)
assert not hasattr(imp, 'init_builtin')
assert not hasattr(imp, 'init_frozen')
imp.init_frozen('xy
