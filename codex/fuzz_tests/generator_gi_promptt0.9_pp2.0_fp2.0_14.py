gi = (i for i in ())
# Test gi.gi_code is the code object
# required by 3.3+ inspect.iscode
assert gi.gi_code.co_flags & 0x20


def test_types_mappingproxy():
    class M(Mapping):

        def __getitem__(self, key):
            return key

        def __len__(self):
            return 1

        def __iter__(self):
            yield 'a'

    m = M()
    pm = types.MappingProxyType(m)
    for name in dir(pm):
        if name[0] == '_':
            continue
        obj = getattr(pm, name)
        if callable(obj) and name not in ('keys', 'values', 'items', 'get'):
            with raises(TypeError):
                obj()
    assert pm['a'] == 'a'
    assert pm.get('a') == 'a'
    assert pm.get('b') is None
    assert pm.keys() == dict_keys(['a'])
    assert pm.values() == dict_values(['a'])
    assert
