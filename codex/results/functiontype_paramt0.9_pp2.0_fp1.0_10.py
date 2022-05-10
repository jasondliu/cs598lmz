from types import FunctionType
list(FunctionType(code,globals(),name="fn"))
Out[66]: [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
</code>
It's a good idea to disassemble bytecode to learn how the 'while 0' loop work.
<code>In [67]: import dis

In [68]: dis.dis(code)
  2           0 LOAD_GLOBAL              0 (range)
              2 LOAD_CONST               1 (3)
              4 CALL_FUNCTION            1
              6 GET_ITER
        &gt;&gt;    8 FOR_ITER               56 (to 68)
             10 STORE_FAST               0 (a)

  3          12 SETUP_LOOP              32 (to 48)
             14 LOAD_CONST               2 (0)
             16 SETUP_WITH              24 (to 42)

  4          18 SETUP_LOOP               8 (to 28)
             20 LOAD_FAST                0
