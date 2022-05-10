import io
class File(io.RawIOBase):
  pass
class IO(io.IOBase):
  pass
'''

  def test_deps_trace(self):
    self.enable_modules, self.disable_modules = ['thread'], []

    self.btest('trace_deps.py', expected='1\n2\nC\n', args=['nostdlib'])

  def test_ignore_light_dylibs(self):
    create_test_file('lib.js', '''
      mergeInto(LibraryManager.library, {
        hello__deps: ['hi'],
        hello: function() {
          return  Module['hi']+1;
        },
        hi: 3,
      });
    ''')

    create_test_file('main.c', r'''
      #include <stdio.h>
      extern int hello(void);
      int main(void) {
        printf("%d.\n", hello());
        return 0;
      }
    ''')

    self.set_setting('IGNORE_CLOSURE_COMPILER
