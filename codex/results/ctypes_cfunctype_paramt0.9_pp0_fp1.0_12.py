import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

def log_func(level, obj):
    """Default logger based on the logging module"""
    try:
        handler = getattr(logging, obj.log_levels[level].upper())
    except AttributeError:
        handler = logging.debug
    return lambda x: handler(x.decode('utf-8'))

# The list of all available methods for the Get/SetOption() functions.
# The list is provided by frei0r itself. Many methods are obsolete
# but are still available here for backward compatibility. 
#
# Deprecated count:
#
# modes - independent, filter, source
# blending_modes - normal, multiply, screen, overlay, diff, screen100, add100, add200, sub100, darken, lighten, dodge, burn, hardlight, softlight, grainextract, grainsolo, grainmerge
#
OBJECT_METHODS = {
    
    # Mode
    'modes': 'source', # independent, filter, source
    'blending_modes': 'normal', # normal, multiply, screen
