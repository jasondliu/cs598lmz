fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__flags__ = 0
fn()"""
        self.assert_raises_typerror(code)
        # check bytecode does not crash
        check_code(code)

    def test_tuple_of_int(self):
        code = """def fn():
    return (0, 1, 2, 3, 4, 5)"""
        dis_code, bc_code = self.get_dis_and_bc_codes(code)
        self.assert_jit_matches(dis_code, bc_code)

    def test_tuple_of_int_load_fast(self):
        code = """def fn():
    a = 0
    return (1, 2, 3, 4, 5, a)"""
        dis_code, bc_code = self.get_dis_and_bc_codes(code)
        self.assert_jit_matches(dis_code, bc_code)

    def test_tuple_of_int_load_deref(self):
        code = """def fn():
    a = 0
    b
