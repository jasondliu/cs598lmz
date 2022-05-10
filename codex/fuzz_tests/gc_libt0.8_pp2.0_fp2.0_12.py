import gc, weakref, inspect

from openalea.core import *
from openalea.core.interface import *
from openalea.core.pkgmanager import PackageManager
from openalea.core.service.ipython import interpreter
from openalea.core.datatype.data_descriptor import DataDescriptor
from openalea.core.datatype.data_descriptor import DictDataDescriptor
from openalea.core.datatype.data_descriptor import GraphDataDescriptor
from openalea.core.datatype.data_descriptor import DataDictDescriptor
from openalea.core.datatype.data_descriptor import DataListDescriptor


class DataDict(dict):
    """
    Class that wraps a dictionnary of data with their descriptor

    >>> dd = DataDict()
    >>> d1 = DataDictDescriptor('d1', description="data 1")
    >>> d2 = DataDictDescriptor('d2', description="data 2")
    >>> dd[d1] = 1
   
