from types import FunctionType
list(FunctionType(lambda i: i + 1, globals(), 'function_name') for i in range(4))
</code>
Версии с <code>exec</code>, как правило, будут работать медленнее, т.к. будет производиться операция компиляции из текста на каждой итерации.

