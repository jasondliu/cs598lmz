import ctypes
ctypes.cast(0, ctypes.py_object).value

# -----------------------------------------------------------------------------
# ctypes.pythonapi
# -----------------------------------------------------------------------------

# ctypes.pythonapi is not available

# -----------------------------------------------------------------------------
# ctypes.resize
# -----------------------------------------------------------------------------

ctypes.resize(ctypes.c_int(1), 2)

# -----------------------------------------------------------------------------
# ctypes.set_conversion_mode
# -----------------------------------------------------------------------------

ctypes.set_conversion_mode("ascii", "strict")
ctypes.set_conversion_mode("ascii", "replace")
ctypes.set_conversion_mode("ascii", "ignore")
ctypes.set_conversion_mode("ascii", "backslashreplace")

ctypes.set_conversion_mode("mbcs", "strict")
ctypes.set_conversion_mode("mbcs", "replace")
ctypes.set_conversion_mode("mbcs", "ignore")
ctypes.set_conversion_mode("mbcs", "backslashreplace")

ctypes.set_conversion_mode("utf
