from types import FunctionType
list(FunctionType(re.compile(r'\d+').search, {}))
# [0, '6']
</code>

