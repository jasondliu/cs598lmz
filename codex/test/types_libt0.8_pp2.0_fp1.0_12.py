import types
types.TypeType = type # oO

################################################################################
# Types
################################################################################

class Type(object):
  """ Base type class """
  def __init__(self, name = "Type"):
    self.name = name

  def __str__(self):
    return self.name

  def __eq__(self, other):
    return self.name == other.name

  def __neq__(self, other):
    return not (self == other)

class TopType(Type):
  """ A type that is compatible with everything """
  def __init__(self):
    Type.__init__(self, "top")

  def get_type(self):
    return NoType()

  def is_type(self):
    return False

  def is_error(self):
    return False

  def is_top(self):
    return True

  def is_static(self):
    return False

  def is_callable(self):
    return False

  def is_class(self):
    return False

