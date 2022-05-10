from types import FunctionType
a = (x for x in [1])
assert type(a) == types.GeneratorType
with pytest.raises(TypeError):
    assert type(1) == types.GeneratorType

# __builtin__.zip
a = zip([1], [2])
assert type(a) == __builtin__.zip
with pytest.raises(TypeError):
    assert type(1) == __builtin__.zip

# __builtin__.range
a = range(5)
assert type(a) == __builtin__.range
with pytest.raises(TypeError):
    assert type(1) == __builtin__.range

# __builtin__.complex
a = complex(1, 2)
assert type(a) == __builtin__.complex
with pytest.raises(TypeError):
    assert type(1) == __builtin__.complex

# fractions.Fraction
a = fractions.Fraction(3, 4)
assert type(a) == fractions.Fraction
with pytest.raises(TypeError):
    assert type(1) == fractions.F
