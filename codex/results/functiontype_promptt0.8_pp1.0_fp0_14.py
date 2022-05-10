import types
# Test types.FunctionType is callable
callable(types.FunctionType)

# Verify that it received the proper parameters
def test_FunctionType_callable():
    assert __ == callable(types.FunctionType)

# Test types.TypeType is callable
callable(types.TypeType)

# Verify that it received the proper parameters
def test_TypeType_callable():
    assert __ == callable(types.TypeType)

# Change the parameter to check your work.
def next_year_birthday(year):
    return '{0}, your next birthday is in {1} days'.format(year, 365)

# Call the function
next_year_birthday(1990)

# Test the function
def test_next_year_birthday_callable():
    assert __ == next_year_birthday(1990)

def next_year_birthday(year):
    return '{0}, your next birthday is in {1} days'.format(year, 365)

# Call the function
next_year_birthday(1990)

# Test the function
def test_next
