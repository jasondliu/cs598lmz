import codecs
codecs.register_error("strict", codecs.ignore_errors)


def get_test_script_path(test_script_name):
    SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(SCRIPT_DIR, "script", test_script_name)


def test_integration_invalid_utf8_input_strict_invalid_utf8_output():
    test_script = get_test_script_path("test_invalid_utf8_input_strict_invalid_utf8_output.py")
    expected_output = "Unkown error\n"
    actual_output = execute_command(["python", test_script])
    assert_strings_equal_ignore_line_endings(expected_output, actual_output)


def test_integration_invalid_utf8_input_strict_invalid_utf8_output_verbose_strict_invalid_utf8_output():
    test_script = get_test_script_path("test_invalid_utf
