import types
types.MethodType(f, None, class_)

class_ = types.new_class('metaclass', (), {}, lambda ns: ns)
class_.__init__ = types.MethodType(f, None, class_)

class_ = types.new_class('metaclass', (), {}, lambda ns: ns)
class_.__init__ = types.MethodType(f, None, class_)

class_ = types.new_class('metaclass', (), {}, lambda ns: ns)
class_.__init__ = types.MethodType(f, None, class_)

class_ = types.new_class('metaclass', (), {}, lambda ns: ns)
class_.__init__ = types.MethodType(f, None, class_)

class_ = types.new_class('metaclass', (), {}, lambda ns: ns)
class_.__init__ = types.MethodType(f, None, class_)

