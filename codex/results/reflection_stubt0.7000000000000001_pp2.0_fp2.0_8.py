fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__

# 生成器作为上下文管理器
import contextlib


class GenCtxManager(contextlib.ContextDecorator):
    def __init__(self, gen):
        self.gen = gen

    def __enter__(self):
        try:
            return self.gen.__next__()
        except StopIteration as e:
            raise RuntimeError("generator didn't yield") from e

    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            try:
                self.gen.__next__()
            except StopIteration as e:
                return
            else:
                raise RuntimeError("generator didn't stop")
        else:
            try:
                self.gen.throw(exc_type, exc, tb)
                raise RuntimeError("generator didn't stop after throw()")
            except StopIteration as exc:
                return exc is not exc
