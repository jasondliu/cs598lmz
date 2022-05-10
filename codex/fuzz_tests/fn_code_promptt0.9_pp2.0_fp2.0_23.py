fn = lambda: None
# Test fn.__code__ is supported
test_fn.__code__ = None

class TestCase:
    def test_apply_callback(self):
        def test_cb(*args, **kwargs):
            assert args[0]

        d = apply_callback(test_cb, ['foo'])
        return d

    def test_apply_callback_with_code(self):
        def test_cb(*args, **kwargs):
            assert args[0]

        d = apply_callback(test_cb, ['foo', 'bar'], ('info_events', True), ('code', test_fn))
        return d

    def test_callback_with_bad_code(self):
        def test_cb(*args, **kwargs):
            assert args[0]

        d = apply_callback(test_cb, ['foo', 'bar'], ('info_events', True), ('code', 192))
        return d

    def test_apply_callback_without_code(self):
        with pytest.raises(TypeError):
            apply_callback("Code is required", 'foo')


class Test
