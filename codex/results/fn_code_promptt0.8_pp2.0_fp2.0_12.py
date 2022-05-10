fn = lambda: None
# Test fn.__code__ and fn.__closure__
        try:
            exec 'def fn(): pass' in locals()
        except TypeError:
            # No code or closure.
            return False
        else:
            return True

def supports_py3k_ge_maint_3_1(python):
    code, stdout = run_python(python, "-c",
            "import sys; print(sys.version_info[:3] >= (3, 1, 0))")
    return code == 0 and stdout.strip() == 'True'

def supports_py_limited_api(python):
    code, stdout = run_python(python, "-c",
            "import sys; print(hasattr(sys, 'getdlopenflags'))")
    return code == 0 and stdout.strip() == 'True'

def supports_py3k_bytes(python):
    code, stdout = run_python(python, "-c",
            "import sys; print(hasattr(sys, 'implementation'))")
    return code == 0 and stdout.strip() == 'True
