import weakref

import pyomo.gdp

def __gdpModelCallback(sender, **kwds):
    """
    Wrapper function for GdpModel._validate to match the expected
    function signature of a validator function.
    """
    sender._validate(**kwds)

class GdpModel(object):

    @property
    def name(self):
        return self._name

    @property
    def model(self):
        return self._model

    @property
    def repn(self):
        return self._repn

    def __init__(self, model=None, name=None, repn=None):
        """
        Constructor

        Args:
            model (:class:`pyomo.core.base.PyomoModel.ConcreteModel`):
                The Pyomo model containing the disjunct/disjunction
            name (str):
                The name of the disjunct/disjunction to be transformed

        Keyword Args:
            repn (pyomo.gdp.Disjunct/Disjunction):
                an instance of
