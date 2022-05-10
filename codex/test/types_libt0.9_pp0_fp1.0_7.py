import types
types.FunctionType = type((lambda:0).__call__)



@contextlib.contextmanager
def fake_args_file(args):
    """;Copied from setup.py"""
    _, fn = tempfile.mkstemp()
    with open(fn, 'w') as f:
        print('\n'.join(args), file=f)
    
    try:
        yield fn
    finally:
        if 0:
            os.remove(fn)


def run_subproc_test_helper(args, func):
    """;Copied from setup.py"""
    with fake_args_file(args) as fn:
        assert_equal(func(['cat',fn]), 0)


def test_subproc_setup_and_run():
    print('Testing setup_and_run...')
    from setup_and_run import _, as_lists, cmd_list_sep, func_exec_mode,\
        add_path, get_tmp_d, get_abs_path
    from setup_and_run import\
        calculate_aws
