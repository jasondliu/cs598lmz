from types import FunctionType
list(FunctionType(cls.__init__.__code__, globals())(**kwargs) for cls, kwargs in reg)
</code>
which is not elegant at the least, and of course requires you to have all the classes in the same module.
Are there any better solutions to this problem?


A:

Quick, dirty and requires Python 3.5+:
<code>from registry import registry
import sys

registry = {name: cls(**params) for name, (cls, params) in registry.items()}
sys.modules[__name__] = registry
</code>
Any import of this module will thus give you the registry, without having to deal with anything.
Also note that the imports from the registry file can be absolute (<code>from xx.yy import bb</code>).

