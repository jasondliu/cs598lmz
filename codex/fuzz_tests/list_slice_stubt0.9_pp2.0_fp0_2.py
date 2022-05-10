import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=b
lst[0]=a
keepalive=[]
lst.append(b)
del lst
"
) (python-tests-look-at "
c=C()
weakref.proxy(c)
" (ignore-import-from-unused)
))
    nil)
  :regexps
  (;; main
   ;; ("\\=\\(The\\|the\\) \\([A-Z]\\|[a-z]+\\) \\([\\-\\+_a-zA-Z0-9\\<>.]+\\)" 1 font-lock-keyword-face)
   ;; ;; doctest lines
   ;; ("^\\(?:\\(?:>>> \\|\\.\\.\\. \\)?\\)\\([^\n]*\\)\\($\\)" 1 font-lock-constant-face)
   (py-test-visible-face-p :value)
   (py-test-visible-face-p :variable))
  :permanent-local t)

(setq python-tests-
