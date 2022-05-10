import mmap

# ------------------------------------------------------------
# Embedded module. 
# A module does not import files to any Python path. Rather, it
# loads modules directly from a string, which can be found in a
# .py file using file.read() or from a .pyc file using mmap()
# ------------------------------------------------------------
class EmbeddedModuleImporter(object):
  
  # NOTE: You may be tempted to set the path
  # in the init method. You must NOT do this,
  # as the import system will try to use the
  # __path__ attribute to find files when
  # importing a module in __loadmodule__. If
  # the __path__ attribute is not empty, you
  # may cause a recursion problem.
  path = None
  
  def find_module(self, fullname, path = None):
    # No directory given? Just use current
    if (path is None):
      path = [os.getcwd()]
    
    # Load from the given directories
    for item in path:
      module_file = self.__findmodule(fullname, item)
