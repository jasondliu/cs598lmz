import types
# Test types.FunctionType
# Get original
print("Original:", types.FunctionType)
# Make a copy
saved = types.FunctionType
# Restore original
types.FunctionType = saved
# Make sure it still works
print("Restored:", types.FunctionType)
# A real hack!
types.FunctionType = lambda : print("Hacked!")
print("Hacked:", types.FunctionType)
# Restore original
types.FunctionType = saved
# Make sure it still works
print("Restored:", types.FunctionType)
