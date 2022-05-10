import _struct from './struct';
+
+export const openDB = path => {
+  const db = _sqlite3.verbose().open(path, {
+    Promise,
+  });
+
+  const modules = {};
+  Object.keys(_struct).forEach(m => {
+    modules[m] = {};
+
+    Object.keys(_struct[m]).forEach(type => {
+      const struct = _struct[m][type];
+
+      modules[m][type] = {
+        select: async query => (await db).all(query),
+        insert: async query => (await db).run(query),
+        getId: async query => (await db).get(`SELECT last_insert_rowid() as id`),
+        createTable: async () => {
+          await db.migrate({ force: 'last' });
+        },
+      };
+
+      if (struct.constraint) {
+        const table = struct.table;
+        const constraint = struct.constr
