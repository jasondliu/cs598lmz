fn = lambda: None
gi = (i for i in ())
fn.__code__ = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
fn.__code__ = gi
"""
        ),
        (
            """
def test(): pass
def test(): pass
""",
            """
def test(): pass
    def test(): pass
"""
        ),
        (
            """
def test():
    def test():
        pass
""",
            """
def test():
    def test(): pass
        def test(): pass
"""
        )
    ])
    def test_can_parse(self, code, extra_code):
        parser = Parser(get_tokens(code))
        parser.parse()
        parser.add_code(extra_code)
        assert parser.can_parse()

    @pytest.mark.parametrize('extra_code', [
        """
def test():
    def test():
        def test():
            pass
""",
        """
def test():
    pass
    def test():
        pass
""",
        """
def test():
    pass

def
