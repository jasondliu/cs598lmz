import selector from './selector';
+
+describe('selector', () => {
+  it('selects', () => {
+    const state = {
+      foo: 'bar',
+    };
+    const select = selector((s) => s.foo);
+    expect(select(state)).toBe('bar');
+  });
+});

