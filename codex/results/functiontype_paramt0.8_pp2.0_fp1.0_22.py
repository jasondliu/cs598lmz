from types import FunctionType
list(FunctionType(text, globals())())
# [1, 2, 3]


# inspect.getclosurevars(func)
# inspect.getmodule(object)
# inspect.getsource(object)
# inspect.getsourcelines(object)
# inspect.getfile(object)
# inspect.getdoc(object)
# inspect.getcomments(object)
# inspect.getargspec(func)
# inspect.getargvalues(frame)
# inspect.formatargspec(formatvalue=str)
# inspect.formatargvalues(frame)
# inspect.currentframe()
# inspect.stack(context=1)
# inspect.trace()
# inspect.getframeinfo(frame, context=1)
# inspect.getouterframes(frame, context=1)
# inspect.getinnerframes(frame, context=1)
