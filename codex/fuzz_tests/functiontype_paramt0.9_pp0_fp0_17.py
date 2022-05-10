from types import FunctionType
list(FunctionType(object.__getattribute__('arbitrary_immutable_fn'), {}).__code__.co_freevars ) 
# ('some val',)

list(FunctionType(object.__getattribute__('arbitrary_mutable_fn'), {}).__code__.co_freevars )
# ('some val',)
</code>

