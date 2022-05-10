import lzma
lzma.__import__("test")
""",
    0,
)

# Test python
check_code(
    f"{test_pycode}", "", "", "", "", "", "", "", "", 0,
)
check_code(f"", "", "", "", "", "", "", "", test_pycode, 0)
check_code("", test_pycode, "", "", "", "", "", "", "", 0)
check_code("", "", test_pycode, "", "", "", "", "", "", 0)
check_code("", "", "", test_pycode, "", "", "", "", "", 0)
check_code("", "", "", "", test_pycode, "", "", "", "", 0)
check_code("", "", "", "", "", test_pycode, "", "", "", 0)
check_code("", "", "", "", "", "", test_pycode, "", "", 0)
check_code("",
