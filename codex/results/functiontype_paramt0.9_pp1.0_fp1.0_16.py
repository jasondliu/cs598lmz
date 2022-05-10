from types import FunctionType
list(FunctionType(lambda x: x.startswith('_'))(dir(str)))

# You can also use these features without the accessor lambdas to get a cleaner look:
#
# [*] [x in y]:
#     [x in y]
#     # instead of
#     (lambda x: x in y)

# [*] [obj.condition]:
#     [obj.condition]
#     # instead of
#     (lambda obj: obj.condition)
#
# [*] [obj.method(args...)]:
#     [obj.method(args...)]
#     # instead of
#     (lambda obj: obj.method(args...))

# [*] [attribute]:
#     [attribute]
#     # instead of
#     (lambda obj: obj.attribute)
#
# [*] [attribute.condition]:
#     [attribute.condition]
#     # instead of
#     (lambda obj: obj.attribute.condition)
#
# [*] [attribute.method(args...)]:
#     [attribute.method(args...)]
#     # instead of
#     (lambda obj
