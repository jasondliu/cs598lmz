fn = lambda: None
gi = (i for i in ())
fn.__code__ = type(lambda: 0).__code__
setattr(gi, 'throw', fn)

# If you are here to classify this bug as invalid, please reconsider and contact
# me first. The issue is more complex than it may appear and classified as
# "invalid" too quickly in the past.
#
# This is a feature request to make ``inspect.isgenerator`` more robust with
# respect to poorly behaved iterators and generators.
#
# The original motivation for this issue was to properly handle badly behaved
# coroutines (ex., with a missing ``__await__`` method), documented as an
# **Anti-Pattern** in PEP 492, but there are other use cases, too.
#
# In this discussion, a "coroutine" refers to an awaitable object based on
# ``types.coroutine`` or ``types.AsyncGenerator``; i.e., the result of calling
# the ``async def`` construct.
#
# The basic problem is that, in CPython 3.7, ``inspect.isgenerator`` raises
# exceptions when it encounters bad iterators or generators.

