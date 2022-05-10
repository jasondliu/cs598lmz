import types
types.MethodType(lambda self: self.v.set_text(self.state.text), Button)

def button_set_text(self, text):
    self.v.set_text(text)

Button.set_text = types.MethodType(button_set_text, Button)

print(Button.set_text.__name__)
print(type(Button.set_text))
Button.set_text.__name__ = 'set_text'

button = Button()
button.set_text('hello')
print(button)

# dir(button)

# print(dir(Button))


import types

def set_text(self, text):
    self.v.set_text(text)

Button.set_text = types.MethodType(set_text, Button)



class ClassMethod:
    def __init__(self, f):
        self.f = f

    def __get__(self, instance, owner):
        return lambda *args: self.f(owner, *args)


