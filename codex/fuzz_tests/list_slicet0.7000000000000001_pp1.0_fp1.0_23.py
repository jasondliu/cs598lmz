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
del keepali0e,lst
"use strict";function e(e){return"function"==typeof e}function t(e){return"number"==typeof e}function n(e){return"string"==typeof e}function r(e){return e===!!e}function i(e){return e===!0}function o(e){return e===!1}function a(e){return e===+e}function s(e){return e===parseFloat(e)}function u(e){return e===parseInt(e,10)}function c(e){return!(e===null||e===void 0)}function l(e){return e===null||e===void 0}function f(e){return"[object Array]"===Object.prototype.toString.call(e)}function p(e){return"[object Date]"===Object.prototype.toString.call(e)}function h(e){return"[object RegExp]"===Object.prototype.toString.call(e)}function d(e){return"[object Object]"===Object.prototype.toString.call(e)}function m(e){return
