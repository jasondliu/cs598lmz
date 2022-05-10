import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    select.select([], [F()], [], 0)

try:
    import _tkinter
    import tkinter
    import tkinter.test.support
except ImportError:
    pass
else:
    def test_tkinter_mutated():
        a = []

        def on_click():
            test_tkinter_mutated()
            a.append(0)

        root = tkinter.Tk()
        btn = tkinter.Button(root, text="hello", command=on_click)
        btn.pack()
        btn.event_generate("<Button-1>")
        btn.event_generate("<Button-1>")

def test_processor_mutated():
    a = []

    class P:
        def close(self):
            test_processor_mutated()
            a.append(0)

    pool = multiprocessing.Pool()
    pool.apply_async(test_processor_mutated, callback=P().close)
    pool.close()
   
