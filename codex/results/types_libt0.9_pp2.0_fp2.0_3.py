import types
types.simple_types = types.StringTypes + types.IntType + types.LongType + types.FloatType

#~ XFrame = genui.XFrame

class HyPython(object):
    def __init__(self, logger=None):
        assert(isinstance(logger, logging.Logger))
        self.logger = logger or logging.getLogger(__name__)
        self.J = None

    def get_assert(self, expected, actual):
        return '''assert(%s == %s)''' % (expected, actual)
    
    def get_class(self, name, parent=object, members={}):
        return '''
class %s(object):
    pass''' % name
    
    def get_declare(self, name, value):
        return '%s = %s' % (name, value)
    
    def get_def(self, name, parent, members):
        return '''
def %s(%s):
    pass''' % (name, ', '.join(members.keys()))
    
   
