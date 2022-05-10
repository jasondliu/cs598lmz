import selectionSort from './selectionSort';
+
+describe('Selection Sort', () => {
+  it('should return an array', () => {
+    expect(Array.isArray(selectionSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))).toBeTruthy();
+  });
+
+  it('should sort the array', () => {
+    expect(selectionSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92])).toEqual([1, 1, 2, 2, 4, 8, 32, 43, 43, 55, 63, 92, 123, 123, 234, 345, 5643]);
+  });
+});

