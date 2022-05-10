fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# '''
# stack -> [10, 2, 3]
# '''
# from functools import partial
#
#
# def pop_while(stack, condition):
#     element = stack[-1]
#     if condition(element):
#         stack.pop()
#         condition = partial(pop_while, condition)
#     return element
#
#
# def push(stack, element):
#     stack.append(element)
#     return element
#
#
# def evaluate_until(stack, condition):
#     while condition(stack):
#         evaluate_until(stack, condition)
#     element = stack.pop()
#     return element
#
#
# def evaluate(stack, element):
#     if element in ('+', '*'):
#         a, b = evaluate(stack, element), evaluate(stack, element)
#         evaluate_until(stack, lambda s: s[-1] not in (a, b))

