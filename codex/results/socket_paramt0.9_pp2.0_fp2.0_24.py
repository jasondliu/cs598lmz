import socket
socket.if_indextoname("8")

def test_function():
    print("This is a test function")

test_function()

test_width = 20


def print_test():
    print("test")
    width = 30
    print("width: " + str(width))


print_test()


def add_two_values(val_one, val_two):
    print("Adding two values")
    total = val_one + val_two
    print("total: " + str(total))
    return total


x = add_two_values(1, 2)
print("x: " + str(x))


def change_first_value(val_one, val_two):
    print("val_one: " + str(val_one))
    val_one = "changed value"
    print("val_one: " + str(val_one))


change_first_value("original", "not changed")


# Note - Python is "pass by assignment" so lists, dictionaries, and other types are passed by reference
def change_first_value_in_list(
