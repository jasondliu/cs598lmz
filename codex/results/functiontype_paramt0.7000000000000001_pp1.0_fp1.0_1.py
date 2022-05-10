from types import FunctionType
list(FunctionType(list, list))
# Для получения списка всех атрибутов объекта можно воспользоваться специальной функцией dir. В качестве аргумента функции можно указать как объект, так и имя объекта (str).
dir(list)
dir(str)
dir(list())
dir([])
dir({})
dir(set)
dir(int)
dir(bool)
dir(float)
dir(object)
dir(object())
dir()
# При
