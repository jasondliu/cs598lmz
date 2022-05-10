import gc, weakref

from rpython.rtyper.annlowlevel import llhelper
from rpython.rtyper.rmodel import inputconst, log
from rpython.rtyper.rpbc import AbstractFrozenPBCRepr
from rpython.rtyper.rpbc import AbstractMethodCache, AbstractAttrCache, AbstractClassAttrCache
from rpython.rtyper.robject import pyobj_repr, new_method_repr
from rpython.rtyper.error import TyperError
from rpython.rtyper.extregistry import ExtRegistryEntry
from rpython.flowspace.model import Constant
from rpython.rlib.objectmodel import compute_identity_hash
from rpython.rlib.unroll import unrolling_iterable
from rpython.tool.sourcetools import func_with_new_name


def rtype_new_instance(hop):
    from rpython.rlib.objectmodel import instantiate
    [v_class] = hop.inputargs(hop.r_result)
    cname = hop.inputconst(ll
