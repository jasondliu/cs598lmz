import types
types.ModuleType.__repr__ = lambda self: '<module %s>' % self.__name__


class Element(object):
    """Factory for creating a list of various element classes."""
    def make_row(self): return Row()
    def make_cell(self): return Cell()
    def make_item(self): return Item()
    def make_cubic(self): return Cubic()
    def make_quadratic(self): return Quadratic()
    def make_triangle6(self): return Triangle6()
    def make_quadratic6(self): return Quadratic6()
    def make_triangle10(self): return Triangle10()

    def make(self, type_name):
        if type_name == 'Row': return self.make_row()
        elif type_name == 'Cell': return self.make_cell()
        elif type_name == 'Item': return self.make_item()
        elif type_name == 'Cubic': return self.make_cubic()
        elif type_name == 'Qu
