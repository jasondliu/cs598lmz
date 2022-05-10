fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# str.isdigit("0.") must raise TypeError.
# CPython raises ValueError instead.
# str.isdigit() calls PyUnicode_IsDigit() which calls PyUnicode_ToDigit()
# which calls unicode_isdecimal() which calls __find_spec__().
# Python 3.9 issue 9467.
for exc in TypeError, ValueError:
    try:
        str.isdigit("0.")
    except exc:
        print("ok [pending]")
    else:
        print("not ok")
