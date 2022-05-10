import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
while keepali0e:keepali0e.pop()
'''
    gcc -O2 -c $i -o $o
  done
  [[ -r "$cwd/../python-plugin.so" ]] || \
    python <<'    EOF'
import sys,os,ctypes
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
c=ctypes.CDLL(os.path.join(path,'python-plugin.so'))
c.python_plugin_initialize_lto(os.path.join(path,'python-plugin.so'))
c.python_plugin_finalize_lto()
c.python_plugin_initialize_lto(os.path.join(path,'python-plugin.so'))
c.python_plugin_finalize_lto()
EOF
fi
if [[ "$0" == "${BASH_SOURCE[0]}" ]]; then
  "$0" -i <(echo "$py_src")
fi
