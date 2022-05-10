import types
types.ModuleType.__repr__ = path_repr


class override_specification:
    """Overrides the specification from the file that was just imported
    
    The attributes expected on an override specification are:
    * 'spec': A dictionary of option name/values to override.
    * 'path': The path in the source tree of files to override.
        overrides with the same path override each other in the order they
        were called.
    """
    
    def __init__(self, spec):
        self.spec = spec
        self.path = spec["path"]
        if self.path[0] != '/':
            self.path = os.path.relpath(self.path, "../")
        if self.path[0] != '/':
            self.path = "/" + self.path
    
    def __lt__(self, other):
        # Reversed sorting order
        return self.path > other.path

def get_package_version(directory):
    """Returns the version string from the installed package"""
    
    # Get the path to the specification
