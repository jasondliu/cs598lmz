gi = (i for i in ())
# Test gi.gi_code.co_lnotab and make sure that we can access the
# four bytes (instructions) beyond the end of the table.
def f():
    for i in range(20):
        x = i
    for i in range(100):
        x = i
    for i in range(200):
        x = i
    import sys
    for i in range(100):
        if i % 10 == 0:
            sys.exc_clear()
        x = i
    return x
def main():
    ensureskip()
    test(
        f(), 89,
        """\

        This is a test of the skip back instruction in LOAD_CONST,
        implemented by two bytes (00 01) at the end of the co_lnotab
        that are not counted in co_lnotab. It also tests the end of
        the code object.
        Here's how it works:
        - 'i' is loaded from an empty generator, which is an unbound
          load (generator.gi_code.co_name is None), and a
          LOAD_GLOBAL
