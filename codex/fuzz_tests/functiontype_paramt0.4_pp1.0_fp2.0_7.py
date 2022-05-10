from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['<lambda>']

# Код лямбда-функции не имеет имени в коде, поэтому в именах переменных она не указывается.

# Получить можно и имена всех переменных, объявленных в лямбда-функции:

from types import FunctionType
list(FunctionType(lambda x: None, {}).__code__.co_varnames)

# ['x']

# Как видит
