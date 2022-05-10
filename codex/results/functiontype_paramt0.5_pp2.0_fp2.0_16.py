from types import FunctionType
list(FunctionType(lambda x:x,globals()).__code__.co_consts)

# ['<code object <lambda> at 0x7f0e8b400f30, file "<stdin>", line 1>',
#  '<code object <lambda> at 0x7f0e8b400f30, file "<stdin>", line 1>',
#  '<code object <lambda> at 0x7f0e8b400f30, file "<stdin>", line 1>',
#  100,
#  '<code object <lambda> at 0x7f0e8b400f30, file "<stdin>", line 1>',
#  '<code object <lambda> at 0x7f0e8b400f30, file "<stdin>", line 1>',
#  '<code object <lambda> at 0x7f0e8b400f30, file "<stdin>", line 1>',
#  '<code object <lambda> at 0x7f0e8b400f30, file "<stdin>", line 1>',
