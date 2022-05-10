from types import FunctionType
list(FunctionType(lambda:None).__code__.co_code)

print("\n", "*"*30, "tuple", "*"*30)
print("tuple(['a', 'b', 'c'])", "\n", tuple(['a', 'b', 'c']))
print("tuple({1, 2, 3})", "\n", tuple({1, 2, 3}))
print("tuple('abc')", "\n", tuple('abc'))
print("tuple(range(0, 3))", "\n", tuple(range(0, 3)))
print("tuple(c for c in ['a', 'b', 'c'])", "\n", tuple(c for c in ['a', 'b', 'c']))

print("\n", "*"*30, "iter", "*"*30)
print("iter('abc')", "\n", iter('abc'))
print("iter(range(0, 3))", "\n", iter(range(0, 3)))
print("iter(['a', 'b', 'c'])", "\n", iter(
