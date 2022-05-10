import ctypes
import ctypes.util
import threading
import sqlite3

_asan_lib = None
# TODO: consider whether this should be a separate module.
# TODO: fully document interface and features.

def _find_asan_lib():
    # Using ctypes.util.find_library won't work when cross-compiling.
    libs = [
        "__asan_preinit", # in asan library.
        "__interceptor_preinit" # in llvm-symbolizer library.
    ]
    if sys.platform == "darwin":
        # Find library location.
        # Deployment versions of Clang puts libraries in lib/ like this:
        # libclang_rt.asan_osx_dynamic.dylib ->
        #   ../lib/clang/5.0.0/lib/darwin/libclang_rt.asan_osx_dynamic.dylib
        # Development versions of Clang puts libraries in lib/ like this:
        # libclang_rt.asan_osx_dynamic.dylib ->
        #   ../lib/darwin/libclang_
