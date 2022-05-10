from types import FunctionType
list(FunctionType(lambda a, b: a + b, globals(), 'f') for a in range(2, 9) for b in range(2, 9) if a > b)

instructors = ['Reynal', 'Miguel', 'Daniel', 'Mercedes', 'Kelvin']

list(filter(lambda name: len(name) <= 5, instructors))

list(filter(lambda name: len(name) <= 5, ['Miguel', 'Kelvin', 'Juan', 'Kris']))

simple_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
}

# map(lambda x: simple_dict[x], [1, 2, 3, 4])
[simple_dict[x] for x in [1, 2, 3, 4]]

names = ['Ocampo', 'Pérez', 'Alcántara', 'Ramos']
list(map(lambda name: name.upper(), names))

weight = [80, 76, 127
