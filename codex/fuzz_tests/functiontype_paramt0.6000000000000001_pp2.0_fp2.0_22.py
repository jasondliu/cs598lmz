from types import FunctionType
list(FunctionType(f.__code__, globals(), 'f').__globals__.keys())

# %%
# Example 6-26. A decorator that returns a function
def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')

target()
target

# %%
# Example 6-27. A decorator that returns a function with arguments
registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()

# %%
# Example 6
