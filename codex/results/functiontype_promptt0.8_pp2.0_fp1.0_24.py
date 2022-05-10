import types
# Test types.FunctionType
def test_type_function_object():
    assert isinstance(is_prime, types.FunctionType)

def test_type_function_object():
    assert isinstance(add_digits, types.FunctionType)

def test_type_function_object():
    assert isinstance(look_for_key, types.FunctionType)

# Test is_prime()
def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(11) == True
    assert is_prime(12) == False
    assert is_prime(13) == True
    assert is_prime(14) == False
    assert is_prime(15) == False
    assert is_
