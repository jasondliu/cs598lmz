import types
types.SimpleNamespace(x=1)

import collections
collections.namedtuple('Person', ['name', 'age'])

from collections import namedtuple
Person = namedtuple('Person', ['name', 'age'])

from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int

p = Person('Bob', 23)
p.name
p.age

from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int
    def __add__(self, other):
        return Person(self.name + other.name, self.age + other.age)

p1 = Person('Bob', 23)
p2 = Person('Alice', 19)
p3 = p1 + p2
p3.name
p3.age

from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int
    def __eq__(self, other):
        return self.name == other.name and self.age
