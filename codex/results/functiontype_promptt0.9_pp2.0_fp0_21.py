import types
# Test types.FunctionType
@dsl.pipeline(
    name='mypipeline',
    description='a basic pipeline'
)
def myfn(arg1='abc', arg2='xyz', arg3=123):
    pass
_ = _TestPipeline(
    dsl_func=myfn,
    name='mypipeline',
    description='a basic pipeline',
    input_args={},
    output_args={}
)
# Test class types.
class A:
    def __init__(self, arg1='abc', arg2='xyz', arg3=123):
        pass
@dsl.pipeline(
    name='mypipeline',
    description='a basic pipeline'
)
def myfn2(arg1='abc', arg2='xyz', arg3=123):
    pass
_ = _TestPipeline(
    dsl_func=myfn2,
    name='mypipeline',
    description='a basic pipeline',
    input_args={},
    output_args={}
)
# Test Dict
class
