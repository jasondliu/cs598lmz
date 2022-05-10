import _struct
import _thread
import _time
import _warnings
import _weakref
import _weakrefset

# import _xxx
_aifc = _imp.new_module('aifc')
sys.modules['aifc'] = _aifc
import aifc
_aifc.error = aifc.Error

_array = _imp.new_module('array')
sys.modules['array'] = _array
_array.error = ValueError

_audioop = _imp.new_module('audioop')
sys.modules['audioop'] = _audioop
_audioop.error = audioop.error

_binascii = _imp.new_module('binascii')
sys.modules['binascii'] = _binascii
import binascii
_binascii.Error = binascii.Error
_binascii.Incomplete = binascii.Incomplete

_cmath = _imp.new_module('cmath')
sys.modules['cmath'] = _cmath
import c
