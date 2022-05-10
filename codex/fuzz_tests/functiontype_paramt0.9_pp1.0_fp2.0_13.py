from types import FunctionType
list(FunctionType() for _ in range(10))

{i: i**2 for i in range(10)}
dict(("key", "value") for _ in range(3))

# !NOTE: 元组内部没有使用括号
tuple("Hello World !")
tuple(i**2 for i in range(10))
tuple({i: i**2 for i in range(10)})
tuple(i**2 for i in range(10) if i % 2)
tuple((i, i**2) for i in range(10))

# !NOTE: 内联和外联  ==> https://www.liaoxuefeng.com/wiki/1016959663602400/1017524398154528
# 问题：为什么内联和外联式生成器要比其他方式快？
# 因
