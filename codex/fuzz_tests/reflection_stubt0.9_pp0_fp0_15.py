fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi()
code_counter += 1

# code.co_consts is not tuple
fn = lambda: None
fn.__code__ = types.CodeType(
    code_counter, 0, 0, 0, 0, b'', (), (), (), '', '', 0, b''
)
code_counter += 1

# code.co_consts is list without int
fn = lambda: None
fn.__code__ = types.CodeType(
    code_counter, 0, 0, 0, 0, b'', [], (), (), '', '', 0, b''
)
code_counter += 1


class ConstsList(list):
    def __eq__(self, other):
        return id(self) == id(other)


# code.co_consts is list without ConstsList
fn = lambda: None
fn.__code__ = types.CodeType(
    code_counter, 0, 0, 0, 0, b'', ConstsList([58]), (), (), '', '', 0, b''
)
code_counter += 1

# code.co
