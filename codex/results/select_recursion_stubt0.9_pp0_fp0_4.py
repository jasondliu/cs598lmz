import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()  # unintended side-effect
            return len(a)

        def read(self):
            return a.pop()

    reader = F()
    a = [reader]
    select.select([reader], [], [], 0.1)
</code>
The problem would be that <code>len(a)</code> would no longer be the same as <code>a.pop()</code> in the call to <code>select()</code> (if <code>a</code> was mutated in the call to <code>fileno()</code>). That is why you are still allowed to call <code>fileno()</code> even if the object isn't closed.
<code>select()</code> works because it simply passes the objects you give it to the <code>poll()</code> object and that in turn just stores them and stores their <code>fileno()</code> to be used when making the <code>poll()</code> call to the kernel (with <code>OsError</code> exceptions thrown if any of the filenos are invalid).
The above is the best answer I could conjure up
