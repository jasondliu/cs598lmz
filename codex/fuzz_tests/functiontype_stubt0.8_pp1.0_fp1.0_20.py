from types import FunctionType
a = (x for x in [1])

# isinstance - проверяет является ли класс обьектом проверяемого класса
print(isinstance(a, GeneratorType))  # true

# issubclass - проверяет является ли класс наследником другого класса
print(issubclass(bool, int))  # true

# help - показывает документацию
print(help(FunctionType))  # посмотрите в консоли

# dir - выводит список полей обьекта
