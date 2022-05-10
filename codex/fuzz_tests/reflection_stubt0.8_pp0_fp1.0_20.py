fn = lambda: None
gi = (i for i in ())
fn.__code__ = c
gi.gi_code = c
c.co_filename = ''
c.co_name = 'foo'

def __bootstrap__():
    global __bootstrap__, __loader__, __file__
    import sys, pkg_resources, imp
    __file__ = pkg_resources.resource_filename(__name__, '_pywrap_tensorflow.so')
    __loader__ = None; del __bootstrap__, __loader__
    imp.load_dynamic(__name__,__file__)
__bootstrap__()
