from types import FunctionType
list(FunctionType(lambda x: f"a{x}")(1).get_closure_cells())

[<cell at 0x0000021A4A7E4A08: int object at 0x0000021A4A7DD7C0>, <cell at 0x0000021A4A7E4A88: function object at 0x0000021A4A753360>]

>>> 
>>> SRC
def f(x):
  def g(y):
    def h(z):
      def i(w):
        def j(u):
          def k(v):
            def l(t):
              return f'{t}{u}{v}{w}{x}{y}{z}{f}{g}'
            return l
          return k
        return j
      return i
    return h
  return g

>>> CODE = compile(SRC, "<string>", "exec")
>>> exec(CODE)
>>> l = j(1)(2)(3)(4)(5)(6)(7)
>>> l(8)
'87654321<function f at 0x0000023BB553
