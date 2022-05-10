import gc, weakref
import random, bisect

# NOTE: Uncomment the lines with the 'pass' statement once the the
# other methods are implemented.

class Person(object):
    """Basic class for a person"""

    def __init__(self, name, birth_year, email=None):
        self.name = str(name)
        self.birth_year = birth_year
        self.email = email

    def get_person(self, people):
        """
        Gets the object in the list people with the same
        birth year and name.
        """
        for person in people:
            if person.name == self.name and person.birth_year == self.birth_year:
                return person
        return "false"

    def __lt__(self, person):
        """
        returns True if this person's name is lexicographically
        less than the other person's name.
        """
        if type(person) == type(self):
            if self.name < person.name or self.name == person.name and self.birth_year < person.birth_year:
               
