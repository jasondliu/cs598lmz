fn = lambda: None
# Test fn.__code__.co_filename == "<stdin>"
# Test fn.__code__.co_firstlineno == 1

# Test fn.__code__.co_flags & CO_VARARGS == CO_VARARGS
# Test fn.__code__.co_flags & CO_VARKEYWORDS == CO_VARKEYWORDS
# Test fn.__code__.co_flags & CO_NESTED == CO_NESTED
# Test fn.__code__.co_flags & CO_GENERATOR == CO_GENERATOR
# Test fn.__code__.co_flags & CO_NOFREE == CO_NOFREE
# Test fn.__code__.co_flags & CO_FUTURE_DIVISION == CO_FUTURE_DIVISION
# Test fn.__code__.co_flags & CO_FUTURE_ABSOLUTE_IMPORT == CO_FUTURE_ABSOLUTE_IMPORT
# Test fn.__code__.co_flags & CO_FUTURE_WITH_STATEMENT == CO_FUTURE_WITH_STAT
