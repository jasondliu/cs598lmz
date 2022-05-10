import gc, weakref

from .objects import W_Object, W_Root, String, W_Fixnum, W_Float, \
        W_String, W_Array, W_Hash, W_Proc, W_Module, W_Class, W_Method, \
        W_UnboundMethod, W_Binding, W_BlockProc, W_Fiber, W_Data, \
        W_Symbol, W_Channel, W_Time, W_Dir, W_True, W_False, W_Nil, \
        W_Match, W_Match2, W_Range, W_Struct, W_Env, W_Enumerator, \
        W_Exception, W_Pointer, W_Numeric, W_Regexp, W_Signature, \
        W_Masgn, W_Undef, W_MethodMissing, W_UserData, W_Complex
from . import ops
from rupypy.utils import memoize
from rupypy.constants import ID_ALLOCATOR, ID_CALL, ID_ATTR_WRITE, ID_EQQ
