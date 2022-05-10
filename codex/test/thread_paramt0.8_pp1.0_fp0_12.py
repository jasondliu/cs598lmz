import sys, threading
threading.Thread(target=lambda:
                 sys.stdout.write("Hello from other thread\n")).start()
                                                                
print("Main thread")

# We can call functions but we don't have access to locals and globals
def foo(x):
  return x * 2

my_globals = {
  "foo": foo,
  "x": 10,
}

exec("""
print(foo(x) == x * 2)
""", my_globals)

# The expression eval is basically an alias to exec
my_globals["x"] = 20
print(eval("x * 2", my_globals))
print(eval("""
def bar():
  return 10

bar()
""", my_globals))

try:
  eval("x")
except NameError:
  print("NameError is expected")

# Lambda expression
my_globals["lam"] = eval("lambda x: x * 2")
print(my_globals["lam"](3))
print(my_globals["lam"](4))


