import gc, weakref
+import os
+
+
+def multiple_of_any(value, divisors, minimum=2):
+    '''
+    Checks if a value is a multiple of any number in the list of divisors after a minimum value.
+    :param value: integer to be checked
+    :type: int
+    :param divisors: list of integers to be checked
+    :param minimum: minimum value to start search
+    :type: int
+    :return: a divisor
+    :rtype: int
+    '''
+    while minimum <= value:
+        for div in divisors:
+            if value % divisor == 0: return div
+        minimum += 1
+    return None
+
+
+class Factors:
+    '''
+    The factors class consists of a value and a list of factors that divide completely into the value.
+    A cached copy is kept on disk to facilitate faster loading when the same number is used.
+    '''
+    __slots__ = ('value', 'factors')
+   
