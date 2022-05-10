gi = (i for i in ())
# Test gi.gi_code.co_name -- but can't use is_() here, co_name is None or str
def test_genexp_gi_code():
    g = lambda: [i for i in (1,2)]
    assert g().gi_code.co_name == '<listcomp>'
    assert bool(g().gi_frame)
    assert g().gi_yieldfrom is None
    g = lambda: (i for i in (1,2))
    assert g().gi_code.co_name == '<genexpr>'
    assert bool(g().gi_frame)
    assert g().gi_yieldfrom is None
test_genexp_gi_code()

def test_closure():
    def l():
        lst = []
        lst.append(lambda : lst)
        lst.append(lst)
        return lst
    assert l()[0]() is l()[1]

def test_dict_correct_builtin_from_dict():
    def f(): pass
    f.func_dict = dict(a=42)

