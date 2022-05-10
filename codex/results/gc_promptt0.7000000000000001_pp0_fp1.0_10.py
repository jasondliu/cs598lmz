import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() to verify everything is collected.
gc.collect()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

# Module globals.
_template_cache = {}

# Module functions
def _load_template(name):
    """Load a template file.
    Templates are stored in the templates package.
    """
    global _template_cache
    if name not in _template_cache:
        # Load the template file from the templates package
        _template_cache[name] = _env.get_template(name)
    return _template_cache[name]

def _render_template(name, **kwargs):
    """Render a template."""
    return _load_template(name).render(**kwargs)

# Classes
class _Template(object):
    """A Jinja2 template object."""
    
    __slots__ = ['name', '_template']
    
    def __init__(self, name):
        self.name = name
        self._template = _load_template(name)
        # Register a weak reference to this template
