import ctypes
ctypes.cast(0, ctypes.py_object)

# ___________________________________________________________________________
#
#  PyPy's ctypes
#
# ___________________________________________________________________________

try:
    import _rawffi
except ImportError:
    pass
else:
    def test_rawffi_callback_with_py_object():
        from _rawffi.alt import types
        from _rawffi.callback import CFuncPtr
        from _rawffi.structure import Structure
        from _rawffi.array import Array
        from _rawffi.ptr import _CDataPtr
        from _rawffi.callback import _CDataCallback
        from _rawffi.callback import _CDataCallbackPtr
        from _rawffi.callback import _CDataCallbackProcPtr
        from _rawffi.callback import _CDataCallbackFuncPtr
        from _rawffi.callback import _CDataCallbackFuncProcPtr
        from _rawffi.callback import _CDataCallbackFuncPtrPtr
        from _rawffi.callback import _CDataCallbackFuncProcPtrPtr

