import gc, weakref

class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number
    def __repr__(self):
        return 'Person: ' + self.name + ' ' + self.surname + ' ' + self.number

class Group:
    def __init__(self, *args):
        self.people = list(args)
    def __repr__(self):
        return 'Group: ' + str(self.people)
    def __len__(self):
        return len(self.people)
    def __getitem__(self, key):
        return self.people[key]
    def __iter__(self):
        return iter(self.people)
    def __contains__(self, item):
        return item in self.people
    def append(self, p):
        self.people.append(p)
    def remove(self, p):
        self.people.remove(p)
    def sort(self, key=
