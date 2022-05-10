fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__

fn.__code__ = None
fn.__code__

"""

# ast
"""
import ast

tree = ast.parse(code)
ast.dump(tree)

# ast.fix_missing_locations(tree)

# exec(compile(tree, filename="<ast>", mode="exec"))

"""

# compile
"""
import dis

code_obj = compile(code, filename="<string>", mode="exec")
dis.dis(code_obj)

eval(code_obj)

"""

# eval
"""
eval(code)
"""

# exec
"""
exec(code)
"""

# execfile
"""
execfile("test.py")
"""

# import
"""
import test
"""

# compile
"""
import dis

code_obj = compile(code, filename="<string>", mode="exec")
dis.dis(code_obj)
"""

# pdb
"""
import pdb

pdb.run(code)
"""

