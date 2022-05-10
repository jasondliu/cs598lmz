fn = lambda: None
# Test fn.__code__ to see if it looks like a py2 func and use the class above
# if so
if sys.version_info[0] < 3 and isinstance(fn.__code__, types.CodeType):
    import __builtin__
    code = __builtin__.__import__('code')
    class CodeType(type(fn.__code__), object):
        """A custom CodeType that encodes unicode objects to utf8.
        """

        @property
        def co_names(self):
            """Encode unicode objects to utf8.
            """
            return tuple(_code_encodestr(n) for n in self._co.co_names)

        @property
        def co_freevars(self):
            """Encode unicode objects to utf8.
            """
            return tuple(_code_encodestr(n) for n in self._co.co_freevars)

        @property
        def co_varnames(self):
            """Encode unicode objects to utf8.
            """
            return tuple(_code_
