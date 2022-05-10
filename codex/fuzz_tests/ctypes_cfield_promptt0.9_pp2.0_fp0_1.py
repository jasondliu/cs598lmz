import ctypes
# Test ctypes.CField.
import collections
import sys

def expect(v):
    sys.stdout.write("expect " + str(v) + ", got ")

def run_test(name):
    print("\x1b[31mRunning " + name + "\x1b[0m")
    sys.stdout.flush()
    ctypes.CDLL('build/' + name + '.so').run()
    print("")

run_test("test_record_malloc")
run_test("test_ctypes_gcc_types")
run_test("test_ctypes_date")
run_test("test_ctypes_vector_h")
run_test("test_cfield")
run_test("test_cfield_int")
run_test("test_example_vector")
run_test("test_example_cmove")
run_test("test_ops_for_CField")
run_test("test_cast_in_runtime")
run_test("test_ctypes_farmhash")
run_test("test_ctypes_str")
run_
