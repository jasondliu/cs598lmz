from types import FunctionType
list(FunctionType([],[])._argdefs)

#<codecell>
import re
def get_args(func):
    argregex = re.compile(r'^(?:\s*(?:def|lambda)\s+(\(.+?\))|(.+?):\s*\w+\.(\w+)\s*\(.+?\))')
    m = argregex.match(func.__doc__)
    if m:
        argstxt = m.group(1) or m.group(2)
        if argstxt.startswith(repr(m.group(3))):
            return []
        else:
            return list(map(str.strip,argstxt.split(',')))

def get_doc(func):
    argregex = re.compile(r'^(?:\s*(?:def|lambda)\s+(\(.+?\))|(.+?):\s*\w+\.(\w+)\s*\(.+?\))')
    argstxt = argre
