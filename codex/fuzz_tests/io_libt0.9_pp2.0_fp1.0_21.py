import io.vertx.core.Vertx
+import io.vertx.core.json.JsonObject
+import io.vertx.ext.jdbc.JDBCClient
+
+object DatabaseClient {
+  val DEFAULT_CONFIG = JsonObject().put("url", "jdbc:hsqldb:mem:test?shutdown=true")
+                                   .put("driver_class", "org.hsqldb.jdbcDriver")
+                                   .put("max_pool_size", 30)
+  var client: Option[JDBCClient] = None
+  val defaultUrl = "jdbc:hsqldb:mem:test?shutdown=true"
+  val defaultDriverClass = "org.hsqldb.jdbcDriver"
+  val defaultMaxPoolSize = 30
+}
+
+class DatabaseClient(val vertx: Vertx, val config: JsonObject) {
+  val defaultUrl = "jdbc:hsqldb:mem:test?shutdown=true"
+  val defaultDriverClass =
