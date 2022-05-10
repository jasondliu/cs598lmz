from types import FunctionType
list(FunctionType(lambda x: 2 * x, globals(), 'double')(i) for i in range(10))

# Пример использования генератора в качестве аргумента
# для встроенной функции map
list(map(lambda x: 2 * x, range(10)))

# Пример использования генератора в качестве аргумента
# для встроенной функции filter
list(filter(lambda x: x % 2 == 0, range(10)))

# Пример использов
