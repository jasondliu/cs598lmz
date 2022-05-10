from types import FunctionType
list(FunctionType(lambda x: x + 1, {}, "lambda", (1, ), None))
# [1]
list(map(lambda x: x + 1, iter([1])))
# [2]
list(map(lambda x, y: x + y, iter([1]), iter([2])))
# [3]
list(map(lambda x, y, z: x + y + z, iter([1]), iter([2]), iter([3])))
# [6]
list(map(lambda x, y, z, w: x + y + z + w, iter([]), iter([]), iter([]), iter([])))
# []
list(map(lambda x, y, z, w: x + y + z + w, iter([]), iter([]), iter([]), iter([1])))
# [1]
list(map(lambda x, y, z, w: x + y + z + w, iter([]), iter([]), iter([2]), iter([])))
# [2]
list(map(lambda x, y, z, w: x + y +
