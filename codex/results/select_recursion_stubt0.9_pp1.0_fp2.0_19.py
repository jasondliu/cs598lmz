import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(self)
            raise AssertionError()

    def doit():
        select.select([F()], [], [])
    doit()
    AssertionError:
</code>
This test barfs because the <code>fileno()</code> method raises an <code>AssertionError</code>, and the error propagates into the <code>select.select()</code> call.
And yet <code>F</code> was appended to <code>a</code>, so the object was mutated. How can the error propagate out of code that didn't even run, yet mutated application state?


A:

Clearly <code>F</code> did not actually appear in the <code>select.select</code> call. That would fail from the first list-mutation. You're looking at the side-effects of the first <code>raise</code> -- luckily stack-unwinding occurs in <code>test_select_mutated</code> before <code>select.select</code> is called.

