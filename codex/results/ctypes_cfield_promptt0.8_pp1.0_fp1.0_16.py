import ctypes
# Test ctypes.CFields
import ctypes.wintypes

# Test ctypes.COM_interfaces
assert hasattr(ctypes.COMError, "result")

# Test ctypes.CTypes
assert hasattr(ctypes, 'Array')
assert hasattr(ctypes, 'BigEndianStructure')
assert hasattr(ctypes, 'CFuncPtr')
assert hasattr(ctypes, 'CStructType')
assert hasattr(ctypes, 'DllCanUnloadNow')
assert hasattr(ctypes, 'DllGetClassObject')
assert hasattr(ctypes, 'FormatError')
assert hasattr(ctypes, 'GetLastError')
assert hasattr(ctypes, 'GetLastWinError')
assert hasattr(ctypes, 'HRESULT')
assert hasattr(ctypes, 'IID')
assert hasattr(ctypes, 'LittleEndianStructure')
assert hasattr(ctypes, 'LP_c_char')
assert hasattr(ctypes, 'LP_c_void_p')
assert hasattr(ctypes, 'POINTER')
assert hasattr(ctypes
