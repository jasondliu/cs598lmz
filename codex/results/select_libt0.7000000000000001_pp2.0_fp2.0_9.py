import select_functions
+
+class TestSelectFunctions(unittest.TestCase):
+
+    def setUp(self):
+        self.test_database_url = os.environ["DATABASE_URL"]
+        self.conn = psycopg2.connect(self.test_database_url)
+        self.conn.autocommit = True
+        self.cur = self.conn.cursor()
+
+        self.cur.execute("CREATE TABLE IF NOT EXISTS test_table_1 (id SERIAL PRIMARY KEY, email TEXT UNIQUE NOT NULL, password TEXT NOT NULL);")
+        self.cur.execute("CREATE TABLE IF NOT EXISTS test_table_2 (id SERIAL PRIMARY KEY, email TEXT NOT NULL, password TEXT NOT NULL);")
+        self.cur.execute("CREATE TABLE IF NOT EXISTS test_table_3 (id SERIAL PRIMARY KEY, email TEXT UNIQUE NOT NULL, password TEXT NOT NULL);")
+        self.cur.execute("CREATE TABLE IF NOT EXISTS test
