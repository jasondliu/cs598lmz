import io.micronaut.scheduling.annotation.Async;
+
+import javax.inject.Singleton;
+import java.util.concurrent.CompletionStage;
+
+@Singleton
+public class SimpleChatService {
+
+    @Inject
+    private EventPublisher eventPublisher;
+
+    @Async
+    public void sendMessage(Message message) {
+        eventPublisher.publishEvent(message);
+    }
+}

