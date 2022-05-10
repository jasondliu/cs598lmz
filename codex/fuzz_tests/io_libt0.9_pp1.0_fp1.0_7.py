import io.reactivex.internal.observers.BlockingBaseObserver;
+import io.reactivex.internal.schedulers.ExecutorScheduler;
+import io.reactivex.internal.schedulers.TrampolineScheduler;
+
+import java.util.concurrent.ThreadFactory;
+import java.util.concurrent.TimeUnit;
+
+public class SchedulersTest {
+    public static void main(String[] args) {
+        TrampolineScheduler.instance().scheduleDirect(new Runnable() {
+            @Override
+            public void run() {
+                System.out.println("hello");
+            }
+        });
+
+        new ExecutorScheduler.ExecutorWorker.OverflowStrategy() {
+            @Override
+            public <T> Disposable schedule(io.reactivex.functions.Consumer<T> consumer, T var1, io.reactivex.internal.schedulers.ExecutorScheduler.Worker worker, long delayTime, Time
