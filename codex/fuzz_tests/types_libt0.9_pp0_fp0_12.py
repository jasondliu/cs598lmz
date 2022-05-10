import types
types.ListType=list
types.StringType=str
types.DictType=dict
types.TupleType=tuple
types.UnicodeType=str
#start pyqs

from qs.base import QSBase
from qs.base import QS_DEBUG
from qs.debug import QSDebug
from qs.node import QSNode
from qs.utils import (QSError, QSPack, QSUrlError, QSUrlUnpackError,
                      QSUrlUnpackStructError, QSUrlMoidError, QSUrlKeyError,
                      QSUrlAppError, QSUrlUserError)

from qs.user import QSUser


from  qs.app import QSApp
