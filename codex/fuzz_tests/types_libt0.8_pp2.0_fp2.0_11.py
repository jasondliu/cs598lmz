import types
types.ClassType

# multiple inheritance
class Mother:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"


class Father:
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"


class Child(Mother, Father):
    pass

billy_cyrus = Child()
print(billy_cyrus.eye_color)

# As seen above, if Billy Cyrus doesn't have a value for eye color, he will inherit the Mother's eye color instead because
# Mother was the first class specified in the inheritance.
# To get the Father's instead, we simply switch the order of Mother and Father in the class definition.
