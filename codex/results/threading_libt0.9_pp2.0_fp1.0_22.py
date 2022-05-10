import threading
threading.stack_size(32768)


class TestClass10:
    def test_01(self):
        try:
            cmd = "pymolapi.exe"
            subprocess.Popen([cmd, '-d', 'load test.pdb;load test.pdb', '-w', 'out1.pdb'])
        except Exception as e:
            print(e)
</code>
This code works fine without the <code>threading.stack_size</code> line. To test I changed the <code>CMD</code> and the <code>load</code> pdb files, but the error happens with all files (or at least in the ones I tested so far). 
The error message when adding <code>threading.stack_size</code>:
<code>AttributeError: module '_thread' has no attribute 'stack_size'
</code>
From what I understand from this error, the <code>threading</code> library doesn't have the stack_size attribute, but if I type <code>dir(threading)</code> in the terminal, the attribute <code
