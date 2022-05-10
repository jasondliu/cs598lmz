import ctypes
# Test ctypes.CFUNCTYPE
ctypes.PyDLL(ctypes.__file__).PyErr_SetInterrupt()
# Test callbacks from C++
from ctypes.test import test_cfuncs
# Must work even if the callback raises an exception
assert test_cfuncs.raise_exception(test_cfuncs.testfunc_cb)
EOF
  at_exit { remove_file file }
  system(EnvUtil.compile_env, "#{RbConfig.ruby} #{file}") or exit(false)
end
