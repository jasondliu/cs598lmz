import gc, weakref
import numpy as np
from numpy import matlib

from pyNastran.bdf.fieldWriter import print_card_8
from pyNastran.bdf.bdfInterface.attributes import BDFAttributes


class BDFMethods(BDFAttributes):
    def __init__(self):
        BDFAttributes.__init__(self)
        self.n = 0
        self.i = 0

    def object_attributes(self, mode='public', keys_to_skip=None):
        """
        List the names of attributes of a class as strings. Returns public
        attributes as default.

        Parameters
        ----------
        mode : str
            defines what kind of attributes will be listed
            * "public" - names that do not begin with underscore
            * "private" - names that begin with single underscore
            * "both" - private and public
            * "all" - all attributes that are defined for the object
        keys_to_skip : List[str]; default=None -> []
            names to not consider to avoid deprecation warnings

        Returns
       
