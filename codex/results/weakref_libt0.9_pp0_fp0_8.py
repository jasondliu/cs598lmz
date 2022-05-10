import weakref
from rpython.rtyper.annlowlevel import cast_base_ptr_to_instance
from rpython.rtyper.rclass import AbstractInstanceRepr, AbstractClassRepr,\
     getinstancerepr, getclassrepr
from rpython.rtyper.lltypesystem import lltype, llmemory, rclass
from rpython.rtyper import rmodel
from rpython.rlib import rgc
from rpython.rlib.rarithmetic import r_uint, intmask, LONG_BIT


def retrieve_cts(rtyper, bk):
    ram = rtyper.annotator.bookkeeper
    return rtyper.annotator.translator.annotated[bk.value]

def get_custom_eq_hash(rtyper, cls_repr):
    assert isinstance(cls_repr, AbstractClassRepr)
    return retrieve_cts(rtyper, cls_repr.classdef.custom_eq_hash).learn_annotation(
        rclass.CLASSTYPE)

def get_custom
