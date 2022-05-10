import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]='after-callback'
from rpython.rtyper.annlowlevel import hlstr
print hlstr(lst)

"""
from rpython.rlib.debug import fatalerror
from rpython.rtyper.extregistry import ExtRegistryEntry
from rpython.annotator import model as annmodel
from rpython.annotator.bookkeeper import getbookkeeper
from rpython.rtyper.rmodel import BareBoolRepr, BoolRepr
from rpython.rtyper.lltypesystem import lltype, rclass
from rpython.rtyper.rbuiltin import gen_cast
from rpython.annotator.model import SomeBool


class __extend__(annmodel.SomeInteger):
    def rtyper_makerepr(self, rtyper):
        assert self.knowntype == lltype.Signed
        return SomeLLAbstractConstantIntegerRepr(self.const)

class LLAbstractConstantIntegerRepr(object):
    lowleveltype = lltype.Signed
    is
