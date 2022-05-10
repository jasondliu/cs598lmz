gi = (i for i in ())
# Test gi.gi_code -- a code object


def test_gi_code_generator(gen_instance):
    assert hasattr(gen_instance.gi_code, '__code__')
    assert hasattr(gen_instance.gi_code, 'co_code')
    assert hasattr(gen_instance.gi_code, 'co_consts')
    assert hasattr(gen_instance.gi_code, 'co_freevars')
    assert hasattr(gen_instance.gi_code, 'co_name')
    assert hasattr(gen_instance.gi_code, 'co_names')
    assert hasattr(gen_instance.gi_code, 'co_varnames')
    assert hasattr(gen_instance.gi_code, 'co_cellvars')
    assert hasattr(gen_instance.gi_code, 'co_filename')
    assert hasattr(gen_instance.gi_code, 'co_lnotab')
    assert hasattr(gen_instance.gi_code, 'co_nlocals')
    assert hasattr(gen_instance.gi_code, '
