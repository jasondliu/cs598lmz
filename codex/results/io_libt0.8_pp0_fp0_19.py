import io.github.alexswilliams.serialisation.jackson.demo1
+
+import com.fasterxml.jackson.databind.ObjectMapper
+import io.github.alexswilliams.serialisation.classpath.getFileFromResourcesDirectory
+import io.github.alexswilliams.serialisation.classpath.readFileFromResourcesDirectory
+
+fun main(args: Array<String>) {
+    val mapper = ObjectMapper()
+
+    val file = getFileFromResourcesDirectory("sample1.json")
+    val stream = file.inputStream()
+    val json = stream.bufferedReader().readText()
+    stream.close()
+    require(json.isNotBlank()) { "input JSON is blank at ${file.path}" }
+
+    val javaObject = mapper.readValue(json, Event::class.java)
+    require(javaObject.id?.length == 36) { "input JSON is invalid" }
+
+    val serialised = mapper.writeValueAsString(
