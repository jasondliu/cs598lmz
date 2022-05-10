import types
# Test types.FunctionType == types.LambdaType
types_functiontype_value = types.FunctionType == types.LambdaType

def not_keyword(**kw):
    code = inspect.currentframe().f_back.f_code
    return list(code.co_varnames) == list(kw.keys()) == ["kw"]
# $ echo "from __future__ import print_function; print(not_keyword(**{'kw': 1}))" | ./python -W error::Warning -v -
#   not_keyword is a keyword in version 2.6: not_keyword(**{'kw': 1})
# WARNING: not_keyword is a keyword in version 2.6: not_keyword(**{'kw': 1})
#   result = not_keyword(**{'kw': 1})


## ../../test/keyword_in_2_6.py:14: Warning: not_keyword is a keyword in version 2.6
#
# ../../test/keyword_in_2_6.py:14: warning: not_keyword
