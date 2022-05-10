fn = lambda: None
gi = (i for i in ())
fn.__code__ = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
gi.gi_code = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
fn.__code__.co_code = b"foobarbaz"
gi.gi_code.co_code = b"quuxquuuz"

# NEWBYTECODE
expected_results = [b"foobarbaz", b"quuxquuuz"]

for obj, expected_result in zip((fn, gi), expected_results):
    result = dis.code_info(obj)
    assert result == expected_result
    # check that bytes is allowed as well
    assert dis.code_info(bytes(result)) == expected_result
