import types
types.new_class("BigFatInteger", (int,))

def my_func(arg):
    print("Got", arg)

def main():
    b = BigFatInteger(42)
    print(isinstance(b, int))
    print(isinstance(b, BigFatInteger))
    print(isinstance(b, (BigFatInteger,)))

    my_func(5)
    my_func(b)

    print(b + 1)
    print(b + b)
    print(b * b)
    print(b / b)

    b2 = BigFatInteger(43)
    print("Comparisons", b == b2, b != b2, b < b2)
    print("Math", b + b2, b - b2, b * b2, b / b2, b ** b2)




