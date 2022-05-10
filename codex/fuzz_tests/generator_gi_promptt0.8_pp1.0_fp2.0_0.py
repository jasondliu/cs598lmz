gi = (i for i in ())
# Test gi.gi_code attribute.
print(gi.gi_code)  # <code object <genexpr> at 0x1006a2d20, file "import_genexpr_in_nested_scope.py", line 10>

# Nested scope.
def f():
    gj = (j for j in ())
    # Test gj.gi_code attribute.
    print(gj.gi_code)  # <code object <genexpr> at 0x1006a24f0, file "import_genexpr_in_nested_scope.py", line 10>

f()
