import weakref


from rpython.tool.udir import udir
from rpython.rtyper.rclass import AbstractInstanceRepr, AbstractClassRepr
from rpython.rtyper.lltypesystem import lltype, llmemory, rclass
from rpython.rtyper.lltypesystem.lltype import (Void, Signed, Malloced, Ptr,
    GcStruct, Char, Array, ContainerType, pyobjectptr, PyObject)
from rpython.rtyper.llinterp import LLException
from rpython.rtyper.annlowlevel import (cast_instance_to_base_ptr,
    cast_base_ptr_to_instance, cast_base_ptr_to_instance_maybe)
from rpython.rtyper.error import TyperError, hint
from rpython.rtyper.lltypesystem.lloperation import llop
from rpython.rlib.objectmodel import specialize
from rpython.rlib.rarithmetic import ovfcheck
from rpython.rlib.rstring import StringBuilder
