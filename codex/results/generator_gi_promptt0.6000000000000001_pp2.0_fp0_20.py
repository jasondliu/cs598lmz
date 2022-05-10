gi = (i for i in ())
# Test gi.gi_code.co_name
assert gi.gi_code.co_name == '<genexpr>'
assert gi.gi_frame.f_code.co_name == '<module>'
assert gi.gi_frame.f_code.co_filename == '<string>'

# Test that generator expressions throw StopIteration when exhausted
def genexpr_test():
    gi = (i for i in range(5))
    l = []
    try:
        while True:
            l.append(next(gi))
    except StopIteration:
        return l
assert genexpr_test() == [0, 1, 2, 3, 4]

# Test generator expressions with multiple for clauses
assert list((i, j) for i in range(2) for j in range(2)) == [(0, 0), (0, 1), (1, 0), (1, 1)]

# Test generator expressions with multiple if clauses
assert list(i for i in range(2) if i if i) == [1]

# Test generator expressions with multiple for clauses and if clauses
assert list
