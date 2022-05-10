fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
with captured_output() as (out, err):
    dis.dis(fn)
output = out.getvalue().strip()
print(output)
assert output == "  4           0 LOAD_CONST               0 (<code object <lambda> at " \
            "0x7fafc34fc0d0, file '%s', line 4>)" % __file__

# do not crash in load_genexpr if the closure of the generator is not
# set up yet.
fn = lambda: None
fn.__code__ = (c for c in ())
with captured_output() as (out, err):
    dis.dis(fn)
output = out.getvalue().strip()
print(output)
assert output == "  4           0 LOAD_CONST               0 (<code object <lambda> at " \
            "0x7fafc34fc0d0, file '%s', line 4>)" % __file__

if __name__ == "__main__":
    test_main()
