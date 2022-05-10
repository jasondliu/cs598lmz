gi = (i for i in ())
# Test gi.gi_code


def test_generator_close(gen, capsys):
    with pytest.raises(ValueError) as excinfo:
        gen.close()
    assert "Generator already executing" in str(excinfo.value)

    assert excinfo.typename == "ValueError"


def test_generator_close_throw(gen):
    with pytest.raises(ValueError) as excinfo:
        next(gen)
    assert "Generator already executing" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        gen.close()
    assert "Generator already executing" in str(excinfo.value)


def test_generator_exception(gen):
    with pytest.raises(ValueError) as excinfo:
        next(gen)
    assert "generator raised StopIteration" in str(excinfo.value)


def test_generator_send(gen):
    with pytest.raises(StopIteration) as excinfo:
        gen.send(None)
    assert exc
