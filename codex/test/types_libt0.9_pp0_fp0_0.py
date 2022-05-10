import types
types.FunctionType.cf_locals = lambda : {}

def marker_to_dict(func_obj):
    marker = {}
    marker['path'] = func_obj.__name__
    marker['name'] = func_obj.__name__
    if hasattr(func_obj, 'lp_test_id'):
        marker['external_id'] = func_obj.lp_test_id
    return marker

def pytest_runtest_makereport(item, call):
    if "lp_test_id" in item.keywords:
        if call.excinfo is not None:
            names = [item.name]
            lptest_name = item.keywords['lp_test_id'].args[0]
            names.append(lptest_name)
            for name in names:
                # Find the function definition
                frame = call.excinfo.tb.tb_frame
                while frame is not None:
                    code = frame.f_code
                    if code.co_name == name:
                        break
                    frame = frame.f_
