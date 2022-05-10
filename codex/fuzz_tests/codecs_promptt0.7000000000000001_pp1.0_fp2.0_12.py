import codecs
# Test codecs.register_error
codecs.register_error("test.xmlcharrefreplace", codecs.xmlcharrefreplace_errors.xmlcharrefreplace)

def test_main():
    run_unittest(CodecsModuleTest)

if __name__ == "__main__":
    test_main()
