import types
# Test types.FunctionType, types.LambdaType, types.GeneratorType
test.test_support.run_unittest(
        TypeTestCase,
        TestSequence,
        TestMapping,
        TestCallable,
        TestDictProxy,
        TestClasses,
        TestSubclassing,
        TestRichComps,
        TestJointInheritance,
        TestMixedInheritance,
        TestSlots,
        TestWeakrefs,
        TestFinalization,
        TestDescriptors,
        TestProperties,
        TestClassProperties,
        TestStaticAndClassMethods,
        TestClassAndStaticMethods,
        TestClassMethodFirst,
        TestMetaclass,
        TestMetaclassWithGetattr,
        TestMultiMeta,
        TestMultiBase,
        TestBrokenSlots,
        TestNewStyle,
        TestIndirectNewStyle,
        TestClassAttr,
        TestClassAndStaticMethods,
        TestClassMethodFirst,
        TestMixedClassAndStaticMethods,
        TestDictMethod,
        TestDictMethodWithD
