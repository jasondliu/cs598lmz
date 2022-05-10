import io.reactivex.schedulers.Schedulers;
+
+/**
+ * Created by S.Violet on 2017/8/23.
+ */
+
+public class ObservableSample {
+
+    public static void main(String[] args) {
+
+        //设置完整的背压
+        Flowable.create(new FlowableOnSubscribe<Integer>() {
+            @Override
+            public void subscribe(FlowableEmitter<Integer> e) throws Exception {
+                for (int i = 0; i < 1000; i++){
+                    System.out.println("send->" + i);
+                    e.onNext(i);
+                }
+            }
+        }, BackpressureStrategy.BUFFER).subscribeOn(Schedulers.io())
+                .observeOn(Schedulers.newThread())
+                .subscribe(new Subscriber<Integer>() {
+                    @Override
+                    public void onSubscribe(Subscription s) {
+                        s
