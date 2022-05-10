from types import FunctionType
a = (x for x in [1])
b = ([1, 2], [3, 4])
c = {1: "a", 2: "b"}
d = [1, 2, 3, 4]
e = [1, 2, 3, 4, 5]
f = [1, 2, 3, 4, 5, 6]
g = {"a": 1, "b": 2, "c": 3}
h = {"a": 1, "b": 2, "c": 3, "d": 4}
i = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
j = (1, 2)
k = set([1, 2])
l = set([1, 2, 3])
m = set([1, 2, 3, 4])

def myfunction():
    return 8
n = FunctionType(myfunction.func_code, myfunction.func_globals, "myfunction", myfunction.func_defaults, myfunction.func_closure)


@pytest.mark.parametrize("obj,expected", [(a, False),
                                
