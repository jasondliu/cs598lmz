from types import FunctionType
list(FunctionType('test') for i in range(10))

#[<function test at 0x039E3DF0>, <function test at 0x039E3DD8>,
# <function test at 0x039E3EB8>, <function test at 0x039E3ED0>,
# <function test at 0x039E3EE8>, <function test at 0x039E3F00>,
# <function test at 0x039E3F18>, <function test at 0x039E3F30>,
# <function test at 0x039E3F48>, <function test at 0x039E3F60>]
