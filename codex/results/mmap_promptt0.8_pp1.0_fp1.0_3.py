import mmap
# Test mmap.mmap(0, 1) to ensure it doesn't segfault.
mmap.mmap(0, 1)
print ("Test OK")
"""
        exit_code, stdout, stderr = exec_python3(
            code, __isolated=False)
        self.assertEqual(exit_code, 0)
        self.assertEqual(stdout.decode("ascii"), "Test OK\n")

    def test_exception_in_destructor(self):
        # Issue #14893: segfault when __exit__() method throws an exception.
        code = """if 1:
            import os, tempfile
            fd, name = tempfile.mkstemp()
            try:
                os.close(fd)
                with open(name, 'w') as f:
                    f.write("1")
                    1/0
            finally:
                os.remove(name)
            print("Test OK")
"""
        exit_code, stdout, stderr = exec_python3(
            code, __isolated=False)
       
