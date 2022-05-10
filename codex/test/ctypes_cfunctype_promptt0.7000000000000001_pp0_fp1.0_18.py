import ctypes
# Test ctypes.CFUNCTYPE(...)

# Testing a function pointer specified as an argument to another function:
# PyObject_CallFunction(..., CFUNCTYPE(...), ...)
#
# Testing a function pointer specified as a return value:
# CFUNCTYPE(...)(<function>)

# Enum values are passed to lib.SDL_EventType:
SDL_FIRSTEVENT = 0
SDL_MOUSEMOTION = 1
SDL_MOUSEBUTTONDOWN = 2

# CFUNCTYPE(<type>, <arguments>):
