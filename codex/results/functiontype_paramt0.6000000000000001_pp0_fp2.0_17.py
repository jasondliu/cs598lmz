from types import FunctionType
list(FunctionType(code,globals(),'f'))

# 方法2
from types import FunctionType
from dis import Bytecode
FunctionType.from_code(code,globals(),'f')

# 方法3
from dis import Bytecode
b = Bytecode(code)
b.dis()
b.disassemble()
print(b.dis())

# 方法4
from dis import Bytecode
from dis import dis
dis(code)
# dis(code,file=None)

# 方法5
from dis import dis
dis("s = 'abc';print(s)")

# 方法6
from dis import disassemble
disassemble(code)

# 方法7
from dis import show_code
show_code(code)

# 方法8
from dis import get_instructions
for i in get_instructions(code):
    print(i)
    # print(i.opname)
