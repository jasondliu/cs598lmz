import types
# Test types.FunctionType
assert isinstance(abs, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)
# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)
# Test types.GeneratorType
assert isinstance((x for x in range(10)), types.GeneratorType)
# Test types.CoroutineType
import asyncio
co = asyncio.coroutine(lambda: None)
assert isinstance(co, types.CoroutineType)
# Test types.AsyncGeneratorType
async def agen():
    yield 1
async def build():
    async for value in agen():
        return value
assert isinstance(agen(), types.AsyncGeneratorType)
assert isinstance(build(), types.AsyncGeneratorType)
# Test types.MethodType
class C:
    def method(self):
        pass
assert isinstance(C().method, types.MethodType)
# Test types.BuiltinMethodType
class D:
    def method(self):
        pass
assert isinstance
