from types import FunctionType
list(FunctionType(lambda: 0, globals()) for i in range(4))
# [<function <genexpr>.<lambda> at 0x7f28b6a0af28>,
#  <function <genexpr>.<lambda> at 0x7f28b6a0afa0>,
#  <function <genexpr>.<lambda> at 0x7f28b6a1a048>,
#  <function <genexpr>.<lambda> at 0x7f28b6a1a160>]


print('########################################################################################################################')
print('示例 6-3. listcomp 中可以编写一般的 if 测试和 for 循环，而不仅是 if 语句')
table = [
    '|> > < | |> > <',
    '| < < | | < > |',
    '| | |> | | | |',
    '| | |> | | | |',
    '| < < | | > < |',
    '|
