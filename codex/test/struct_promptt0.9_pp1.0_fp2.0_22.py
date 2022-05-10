import _struct
# Test _struct.Struct('<d')
testmodel.buttons.add_test(test_class=testmodel.SimpleTestCase,
                           test_results=[_struct.Struct('<d').pack(1.000004)],
                           expected=[[float]])
# Test _struct.Struct('<d').unpack
testmodel.buttons.add_test(test_class=testmodel.SimpleTestCase,
                           test_results=_struct.Struct('<d').unpack(_struct.Struct('<d').pack(1.000004)),
                           expected=[[float]])
# Test pwn.pack
testmodel.buttons.add_test(test_class=testmodel.SimpleTestCase,
                           test_results=pwn.pack(2332),
                           expected=[[int]])
# Test pwn.pack(1111111111, signed=True)
testmodel.buttons.add_test(test_class=testmodel.SimpleTestCase,
                           test_results=pwn.pack(1111111111, signed=True),
                           expected=[[int]])
#
