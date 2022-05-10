fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
"""
    )
    assert result.exit_code == 1
    assert "__code__ must be a code object" in result.output


def test_traceback_attribute_error():
    result = runner.invoke(
        cli.main, ["--cov", "-rs", "--tb=short", "-m", "tests/samples/attributeerror.py"]
    )
    assert result.exit_code == 1
    assert "AttributeError: 'NoneType' object has no attribute 'func'" in result.output


def test_syntax_error():
    result = runner.invoke(cli.main, ["--cov", "-rs", "--tb=short", "-m", "tests/samples/syntaxerror.py"])
    assert result.exit_code == 1
    assert "SyntaxError: invalid syntax" in result.output


def test_fatal_error():
    result = runner.invoke(cli.main, ["--cov", "-rs", "--tb=short", "-m", "tests/samples/fatalerror.py"]
