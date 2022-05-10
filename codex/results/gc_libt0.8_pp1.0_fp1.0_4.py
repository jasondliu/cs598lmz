import gc, weakref
import numpy as np

# todo: docstrings
# todo: check for unbounded variables in the objective
# todo: support for binary constraints
# todo: add copy method

_var_counter = itertools.count()
_con_counter = itertools.count()

class Variable(object):
    """The class for all variables in a model.
    """

    def __init__(self, name=''):
        """Creates a variable.

        :param name: the name of the variable.
        """
        self.name = name or 'x%d' % next(_var_counter)
        self.value = None
        self.dual = None


class Constraint(object):
    """The class for all constraints in a model.
    """

    def __init__(self, expr, name='', lb=None, ub=None):
        """Creates a constraint from an expression.

        :param expr: the expression defining the constraint.
        :param name: the name of the constraint.
        :param lb: the lower bound for the constraint
