import selector from "./recipes";
+
+describe("testing recipes selector", () => {
+  test("selector returns empty array when there are no recipes", () => {
+    const store = {
+      recipes: [],
+      ingredients: [],
+      tags: [],
+    };
+    expect(selector(store)).toEqual([]);
+  });
+
+  test("selector returns an array of recipes", () => {
+    const store = {
+      recipes: [{ id: 3 }, { id: 6 }],
+      ingredients: [{ recipe_id: 3 }, { recipe_id: 3 }, { recipe_id: 6 }],
+      tags: [{ recipe_id: 3 }, { recipe_id: 6 }],
+    };
+    expect(selector(store)).toEqual([
+      { id: 3, ingredients: [{ recipe_id: 3 }, { recipe_id: 3 }], tags: [{ recipe_id: 3 }] },
+      { id: 6, ingredients: [{ recipe_id: 6
