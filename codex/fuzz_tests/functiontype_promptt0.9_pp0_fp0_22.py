import types
# Test types.FunctionType and types.BuiltinFunctionType
def isFunction (obj):
  return isinstance(obj, types.FunctionType) or isinstance(obj, types.BuiltinFunctionType)
# ==============================================================================

# ==============================================================================
# Numeric types library.
# ==============================================================================
# Test types.LongType and types.IntType
def isInt (obj):
  return isinstance(obj, types.LongType) or isinstance(obj, types.IntType)
# ------------------------------------------------------------------------------
# Test types.FloatType and types.ComplexType
def isFloat (obj):
  return isinstance(obj, types.FloatType) or isinstance(obj, types.ComplexType)
# ------------------------------------------------------------------------------
# Test types.LongType, types.IntType, types.FloatType and types.ComplexType
def isNumber (obj):
  return isinstance(obj, types.LongType) or isinstance(obj, types.IntType) or isinstance(obj, types.FloatType) or isinstance(obj, types.ComplexType)
# ==============================================================================

# ==============================================================================
# Sequence types library
# =================================================================
