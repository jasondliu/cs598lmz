import io
class File(io.RawIOBase):
    def __init__(self):
        pass
    def write(self, str):
        print("write %s" % str);
# construct
file = File()
# call
file.write("str")

class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0
    def getAge(self):
        return datetime.date.today().year - self.birthday.year - ((datetime.date.today().month, datetime.date.today().day) < (self.birthday.month, self.birthday.day))

# construct
user = User("zhaoch", datetime.date(1990,5,5))
# call
user.getAge() # age(read-only)

# construct
class Animal(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name
    @abstractmethod
    def say(self):
        pass
# call
class Dog(Animal):
    def __init__
