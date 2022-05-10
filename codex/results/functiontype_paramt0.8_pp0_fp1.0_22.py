from types import FunctionType
list(FunctionType(l, globals())() for l in [
lambda: ( S, K, I ),
lambda: ( lambda f: f(f) )(
    lambda f: (
        lambda *a: a[0] if len(a) == 1 else (
            lambda x, y: x(f(y))
        )(*a)
    )
)
])
