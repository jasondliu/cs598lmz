import types
types.SimpleNamespace(**{'a': 1, 'b': 2, 'c': 3})

#%%
import functools
import json

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapped

#%%
@to_json
def get_data():
    return {
        'data': 42
    }

get_data()

#%%
class Person:
    def __init__(self, name, surname, year_of_birth):
        self.name = name
        self.surname = surname
        self.year_of_birth = year_of_birth
        self._age = 0

    @property
    def age(self):
        return datetime.date.today().year - self.year_of_birth

    @age.setter
    def age(self, value):
        self._age = value

    def __str__(self):
        return '{} {}'.format
