import weakref
+
+"""这里需要注意的是, 函数也是对象, 可以通过__closure__属性获得一个cell对象
+
+"""
+
+
+class A:
+    """
+    >>> a = A()
+    >>> a
+    <__main__.A object at 0x1037f1128>
+    >>> weakref.ref(a)
+    <weakref at 0x1035d04a8; to 'A' at 0x1037f1128>
+    >>> weakref.WeakSet([a])
+    WeakSet([<__main__.A object at 0x1037f1128>])
+    """
+    pass
+
+
+class B:
+    """
+    >>> b = B()
+    >>> b
+    <__main__.B object at 0x103a7e470>
+    >>> weakref.ref(b)
