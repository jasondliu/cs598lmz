import io
class File(io.RawIOBase):
    def read(buffer):
        pass
    def close():
        pass
    def __enter__():
        assert False
    def __exit__():
        pass
def open(path, mode='r'):
    pass
""")
        # No stdio
        unit = self.get_unit('stdio.pyi')
        unit.dependencies = []
        unit.analyze(self.build)
        self.assertTypesMatchPytd(unit, """
from typing import IO
File = IO[bytes]
def open(path: str, mode: str='r') -> File:
    pass
""")
        # No typing
        unit = self.get_unit('stdio.pyi')
        unit.dependencies = []
        unit.analyze(self.build, builtins=FakeNamedTupleBuiltins)
        self.assertTypesMatchPytd(unit, """
from mypy_extensions import IO
File = IO[bytes]
def open(path: str, mode: str='r') -> File:
    pass
""")


if __name__ == '
