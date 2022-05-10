import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=lst,a
a.c=lst
keepali0e=weakref.ref(a,callback)
del lst,a
"""
    if sys.version_info > (2, 7):
        self.set_setting('EXECUTABLE_SUFFIX', '')
    else:
        self.set_setting('EXECUTABLE_SUFFIX', '.exe')

  def test_run(self):
    self.check_cmd(self.emcc_args + ['-s', 'ALLOW_MEMORY_GROWTH=1', '-s', 'DOUBLE_MODE=0', path_from_root('tests', 'hello_world.cpp')], 'hello, world!', assert_identical=self.is_wasm())

  def test_run_i64(self):
    self.check_cmd(self.emcc_args + ['-s', 'ALLOW_MEMORY_GROWTH=1', path_from_root('tests', 'hello_world.cpp')], 'hello, world!', assert_ident
