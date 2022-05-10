import threading
threading.stack_size(32768)


class TestClass10:
    def test_01(self):
        try:
            cmd = "pymolapi.exe"
            subprocess.Popen([cmd, '-d', 'load test.pdb;load test.pdb', '-w', 'out1.pdb'])
        except Exception as e:
            print(e)
