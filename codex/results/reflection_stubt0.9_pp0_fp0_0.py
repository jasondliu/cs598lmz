fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = mock.Mock()
fn.__code__.co_filename = os.path.abspath(
    os.path.splitext(os.path.basename(__file__))[0] + ".py"
)

with pytest.raises(TypeError) as e:
    os.fspath(gi)
assert str(e.value) == (
    "expected str, bytes or os.PathLike object, not "
    "generator"
)
