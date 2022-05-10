fn = lambda: None
# Test fn.__code__.co_code[fn.__code__.co_zombieframe] = 0

def test_main(verbose=None):
    test_support.run_doctest(dis, verbose)
    test_support.run_doctest(opcode, verbose)
    test_support.run_doctest(opcode_with_pypy, verbose)
    test_support.run_doctest(py_compile, verbose)
    test_support.run_doctest(py_compile_with_pypy, verbose)
    test_support.run_doctest(compile_command, verbose)

    test_support.run_unittest(
        BasicTest,
        BugTest,
        BytecodeTest,
        CommandLineTest,
        EscapeTest,
        FutureTest,
        OptTest,
        UnquoteTest,
        MiscTest,
        TestCFunctions,
        TestOpcodes,
        )

if __name__ == "__main__":
    test_main(verbose=True
