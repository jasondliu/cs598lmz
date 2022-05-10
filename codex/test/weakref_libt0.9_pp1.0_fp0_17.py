import weakref
from rpython.rlib.rstring import StringBuilder
from rsqueakvm.model.base import W_PointersObject
from rsqueakvm.constants import get_shape, W_INTARRAY0, MARKED, GC_USED
from rsqueakvm.error import PrimitiveFailedError
from rsqueakvm.model.pointers import (
    W_WordsObject, W_BytesObject, W_CompiledMethod, W_PointersObject)
from rsqueakvm.model.display import W_DisplayBitmap, W_DisplayObject
from rsqueakvm.error import PrimitiveFailedError
from rsqueakvm.model.graphics import W_PixmapBitmap, W_AbstractBitmap
from rsqueakvm.model.numeric import W_Float, W_LargeIntegerWord, W_LargeInteger
from rsqueakvm.model.storage_contexts import CPyStorageContext
from rpython.rlib.rjitlog import rjitlog as jl
from rsqueakvm.util.matrix_conv import matrixConvertNamed, matrixConvertString
