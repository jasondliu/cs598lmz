fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__call__()

# test_dict_literal_with_kwargs
d = {i: i for i in range(10) if i % 2}

# test_dict_literal_with_kwargs_and_starred
d = {i: i for i in range(10) if i % 2, **{'a': 1, 'b': 2}}

# test_dict_literal_with_list_comprehension
d = {i: i for i in range(10) if i % 2, **{'a': 1, 'b': 2}, **{i: i for i in range(10) if i % 2}}

# test_dict_literal_with_dict_comprehension
d = {i: i for i in range(10) if i % 2, **{'a': 1, 'b': 2}, **{i: i for i in range(10) if i % 2}, **{i: i for i in range(10) if i % 2}}

# test_dict_literal_with_set_
