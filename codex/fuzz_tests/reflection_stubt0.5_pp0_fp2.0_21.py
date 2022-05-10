fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
# produces an exception.
</code>
Now, you can use this to your advantage.
<code>#!/usr/bin/env python3

import sys

def my_print(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()

def my_input(prompt):
    my_print(prompt, end='')
    return input()

def my_input_int(prompt):
    return int(my_input(prompt))

def my_input_float(prompt):
    return float(my_input(prompt))

def my_input_str(prompt):
    return str(my_input(prompt))

def my_input_list(prompt, item_type=str):
    return list(item_type(x) for x in my_input(prompt).split())

def my_input_tuple(prompt, item_type=str):
    return tuple(item_type(x) for x in my_input(prompt
