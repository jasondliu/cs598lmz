import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return 1
print(fun())
`
  console.log(code)
  try {
    vm.createContext({}, {
      console: 'inherit',
      displayErrors: true
    })
    vm.runInContext(code, sandbox, { filename: 'repl' })
  } catch (ex) {
    console.log(ex)
  }
  // let result = vm.runInNewContext(code, sandbox, { filename: 'repl' });
  // console.log(result);
  return sandbox;
}

replServer();
