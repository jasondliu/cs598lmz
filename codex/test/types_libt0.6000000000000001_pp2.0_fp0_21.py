import types
types.SimpleNamespace

# Define a namedtuple called DataShell
DataShell = namedtuple("DataShell", ["x", "y"])

# Define the first DataShell, named data_shell_1, with x=1, y=2
data_shell_1 = DataShell(1, 2)

# Print out the x-value of data_shell_1
print(data_shell_1.x)

# Define the second DataShell, named data_shell_2, with x=5, y=6
data_shell_2 = DataShell(5, 6)

# Print out the y-value of data_shell_2
print(data_shell_2.y)

# Define a list of DataShells, called data_list
data_list = [data_shell_1, data_shell_2]

# Print out the x-value of the first DataShell in data_list
print(data_list[0].x)


# Define a tuple called my_tuple
