from types import FunctionType
list(FunctionType(lambda x: x, {}).__code__.co_freevars)

# 2.3.9.2.7.1.  Using the current module
list(FunctionType(lambda x: x, {}).__globals__.keys())

# 2.4.1.1.  Built-in Functions
# 2.4.2.  The import Statement
# 2.4.3.  The del Statement
# 2.4.4.  The global Statement
# 2.4.5.  The nonlocal Statement
# 2.4.6.  The assert Statement
# 2.4.7.  The with Statement
# 2.4.8.  The raise Statement
# 2.4.9.  The try Statement
# 2.4.10. The yield Expression
# 2.4.11. The return Statement
# 2.4.12. The break Statement
# 2.4.13. The continue Statement
# 2.4.14. The pass Statement
# 2.4.15. The importlib.util.module_for_loader() Function
# 2.4.16.
