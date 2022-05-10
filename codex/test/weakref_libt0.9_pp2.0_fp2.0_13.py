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

