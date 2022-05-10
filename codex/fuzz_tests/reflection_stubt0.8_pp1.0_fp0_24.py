fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = '<lambda>'
fn.__qualname__ = '<lambda>'
fn.__annotations__ = annotations
functools.singledispatch(fn)


def build_factory(method):
    factory = Mock(spec_set=_MethodFactory)

    factory.method = method

    factory.__call__ = MagicMock(return_value=method)

    def __getattr__(name):
        return getattr(method, name)

    def __init__(*args, **kwargs):
        method.__init__(*args, **kwargs)
        return factory

    factory.__getattr__ = Mock(side_effect=__getattr__)
    factory.__init__ = Mock(side_effect=__init__)

    return factory


def side_effect_str(side_effect):
    if isinstance(side_effect, str):
        return side_effect

    if isinstance(side_effect, tuple):
        side_effect = list(side_effect)

    if isinstance(
