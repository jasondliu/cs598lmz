import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

def test_main():
    # The following tests are based on the Unicode 5.0.0
    # data file DerivedNormalizationProps.txt.
    #
    # The file is a tab-separated file with the following columns:
    #
    # 1. First code point of the range
    # 2. Last code point of the range
    # 3. Canonical_Combining_Class (value 0..255)
    # 4. Canonical_Combining_Class (name)
    # 5. Decomposition_Type (value 0..18)
    # 6. Decomposition_Type (name)
    # 7. Decomposition_Mapping
    # 8. Decimal_Digit_Value (value -1..9)
    # 9. Digit_Value (value -1..9)
    # 10. Numeric_Value (value -1..9)
    # 11. Numeric_Value (double)
    # 12. Numeric_Value (numerator)
    # 13. Numeric_Value (denominator)
    # 14. Numeric_Value
