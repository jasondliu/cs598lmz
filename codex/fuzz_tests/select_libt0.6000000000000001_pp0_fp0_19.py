import selectors

with open("test.txt", "r") as test_file:
    print(test_file.read())

print("-" * 100)
# read(5) reads 5 characters
with open("test.txt", "r") as test_file:
    print(test_file.read(5))

print("-" * 100)
# read(5) reads 5 characters
with open("test.txt", "r") as test_file:
    print(test_file.read(3))
    print(test_file.read(2))
    print(test_file.read(4))

print("-" * 100)
# read(5) reads 5 characters
with open("test.txt", "r") as test_file:
    print(test_file.readline())
    print(test_file.readline())
    print(test_file.readline())

print("-" * 100)
# read(5) reads 5 characters
with open("test.txt", "r") as test_file:
    print(test_file.readlines())

print
